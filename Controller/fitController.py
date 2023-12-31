from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget
from .Models import *
from .entryController import RamBlockDemo, ProcessDemo


class BaseFit(QWidget):
    def __init__(self, mother: QWidget):
        super().__init__()

        self._speed = 1000
        self.ram_block_list: list[RamBlock] = []
        self.free_ram_block_wlist: list[RamBlockDemo] = []
        self.process_list: list[Process] = []

        self.len_free_block = 0
        self.len_process_list = 0

        self._height_list = []
        self.min_ram_cap = 0
        self.min_pro_cap = 0
        self.mother = mother

        self.simulating = True

        self._fitting_speed = 1000
        self._merge_speed = 333
        self._normal_speed = 333

        self.cur_ram_index = 0
        self._end_ram_index = -1
        self.cur_free_ram_id = 0
        self.cur_free_ram: RamBlockDemo | None = None

        self.cur_process: ProcessDemo | None = None
        self._timer = QTimer(self)

        self._timer.timeout.connect(self.update)

    def _set_data(self, ram_list: list[RamBlock], process_list: list[Process]):
        self.ram_block_list = ram_list
        self.process_list = process_list
        if len(self.ram_block_list) != 0 and len(self.process_list) != 0:
            self._setup_rb_entries()
            self._setup_process_entries()

    def _setup_rb_entries(self):
        RamBlock.normalize_model(self.ram_block_list)
        self.min_ram_cap = RamBlock.get_min(self.ram_block_list).capacity
        self.min_pro_cap = Process.get_min(self.process_list).capacity

        self.len_process_list = len(self.process_list)

        self._height_list = []
        self.free_ram_block_wlist = []
        for model in self.ram_block_list:
            rw = RamBlockDemo(model, self.min_ram_cap)
            rwl = RamBlockDemo(model, self.min_ram_cap)
            if model.type_block == 0 or model.type_block == -1:
                self.free_ram_block_wlist.append(rw)
            self.mother.ui.ramBar_lo.addWidget(rw)
            # self.mother.ui.tempBar_lo.addWidget(rwl)
            self._height_list.append(rw.height())
        self.len_free_block = len(self.free_ram_block_wlist)
        self._end_ram_index = self.len_free_block-1

    def _setup_process_entries(self):
        Process.normalize_model(self.process_list)

        for model in self.process_list:
            rw = ProcessDemo(model, self.min_ram_cap)

            self.mother.ui.processBar_lo.addWidget(rw)

    def _reset_rb_entries(self):
        for i in range(self.mother.ui.ramBar_lo.count()):
            self.mother.ui.ramBar_lo.itemAt(i).widget().deleteLater()

        self._setup_rb_entries()

    def _reset_process_entries(self):
        pass

    def set_time(self, t: int):
        self._speed = t

    def start(self, t: int | None = None):
        if t is not None:
            self.set_time(t)
            self._timer.start(t)
        pass

    def pause(self):
        self._timer.stop()

    def play(self):
        self._timer.start(self._speed)

    def update(self):
        self._connect_timer(self._control_process_entry)

    def _connect_timer(self, func, t: int | None = None):
        self._timer.timeout.disconnect()
        self._timer.timeout.connect(func)
        speed = t if t is not None else self._speed
        self._timer.start(speed)

    def _control_process_entry(self):
        if self.mother.ui.processBar_lo.count() == 0:
            self.simulating = True
            self._timer.stop()
            return
        self._setup_cur_process()
        # self._setup_cur_process()
        self._connect_timer(self._control_ram_entry)

    def _control_ram_entry(self):
        # if self.fitting_process:
        self._setup_cur_ram()
        self._connect_timer(self._decision)
        if self.cur_free_ram_id == self._end_ram_index:
            # self.fitting_process = False
            self.cur_free_ram_id = 0
            self._connect_timer(self._control_process_entry)
            self._clear_temp_bar()
            return

        self.cur_free_ram_id = (self.cur_free_ram_id+1)%self.len_free_block


    def _setup_cur_ram(self):
        self.cur_free_ram = self.free_ram_block_wlist[self.cur_free_ram_id]
        self.cur_free_ram.high_light_effect()
        self._brick_stack(self.cur_free_ram.model.index)

    def _setup_cur_process(self):
        temp = self.mother.ui.processBar_lo.itemAt(0).widget()
        self.mother.ui.processBar_lo.removeWidget(temp)
        self.cur_process = ProcessDemo(temp.model, temp.min_ram_cap)
        temp.deleteLater()
        self.mother.ui.tempBar_lo.addWidget(self.cur_process)
        if len(self.free_ram_block_wlist) > 0:
            # print(f'free_id: {self.free_ram_block_wlist[0].model.index}')
            self._brick_stack(self.free_ram_block_wlist[0].model.index)

    def _decision(self):
        if self.cur_free_ram.model.capacity >= self.cur_process.model.capacity:
            self._connect_timer(self._merge_action, round(self._speed * (2 / 3)))
            return
        self._connect_timer(self._control_ram_entry)
        self._normal_effect()

        if self.cur_free_ram_id == 0:
            noAllo = ProcessDemo(self.cur_process.model, self.min_ram_cap)
            self.mother.ui.bottomBar_lo.addWidget(noAllo)

    def _merge_action(self):
        process_model = self.cur_process.model
        ram_model = self.cur_free_ram.model

        if ram_model.capacity < process_model.capacity:
            return
        self.ram_block_list[ram_model.index] = RamBlock(ram_model.index, 2,
                                                        process_model.capacity)
        if process_model.capacity<ram_model.capacity:
            frag_model = RamBlock(-1, -1, ram_model.capacity - process_model.capacity)
            RamBlock.insert_model(self.ram_block_list, ram_model.index + 1, frag_model)

        for model in self.ram_block_list:
            print(f'index: {model.index}; type: {model.type_block} ; cap: {model.capacity}')

        self._clear_temp_bar()
        self._reset_rb_entries()
        self._connect_timer(self._control_process_entry)

    def _normal_effect(self):
        if self.cur_process is not None:
            self.cur_free_ram.normal_effect()

    def kill_oj(self):
        self._timer.stop()
        self.deleteLater()

    def _clear_temp_bar(self):
        for i in range(self.mother.ui.tempBar_lo.count()):
            widget = self.mother.ui.tempBar_lo.itemAt(i).widget()
            widget.deleteLater()

    def _brick_stack(self, cur_rb_id: int):
        self.mother.ui.tempBar_lo.removeWidget(self.cur_process)
        if cur_rb_id > self.cur_ram_index:
            for i in range(self.cur_ram_index, cur_rb_id):
                model = self.ram_block_list[i]
                temp_widget = RamBlockDemo(model, self.min_ram_cap, True)
                self.mother.ui.tempBar_lo.addWidget(temp_widget)
        elif cur_rb_id < self.cur_ram_index:
            self._clear_temp_bar()
            for i in range(0, cur_rb_id):
                model = self.ram_block_list[i]
                temp_widget = RamBlockDemo(model, self.min_ram_cap, True)
                self.mother.ui.tempBar_lo.addWidget(temp_widget)
        self.mother.ui.tempBar_lo.addWidget(self.cur_process)
        self.cur_ram_index = cur_rb_id


class FirstFit(BaseFit):
    def __init__(self, mother_ui: QWidget):
        super().__init__(mother_ui)


class NextFit(BaseFit):
    def __init__(self, mother_ui: QWidget):
        super().__init__(mother_ui)

    def _decision(self):
        if self.cur_free_ram.model.capacity >= self.cur_process.model.capacity:
            self._connect_timer(self._merge_action, round(self._speed * (2 / 3)))
            if self.cur_free_ram_id == len(self.free_ram_block_wlist) - 1:
                self.cur_free_ram_id = -1
            return
        self._connect_timer(self._control_ram_entry)
        self._normal_effect()

        if self.cur_free_ram_id == len(self.free_ram_block_wlist) - 1:
            noAllo = ProcessDemo(self.cur_process.model, self.min_ram_cap)
            self.mother.ui.bottomBar_lo.addWidget(noAllo)
