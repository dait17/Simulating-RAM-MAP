from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget
from .Models import *
from .entryController import RamBlockDemo, ProcessDemo, ProcessOVEntry


class BaseFit(QWidget):
    def __init__(self, mother: QWidget):
        super().__init__()

        self._speed = 1000
        self.block_list: list[RamBlock] = []
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

        self.cur_ram_index = 0
        self._end_ram_index = -1
        self.cur_free_ram_index = 0
        self.cur_free_ram: RamBlockDemo | None = None
        self.cur_process: ProcessDemo | None = None
        self._timer = QTimer(self)

        self._timer.timeout.connect(self.run)

    def set_data(self, ram_list: list[RamBlock], process_list: list[Process]):
        self.block_list = [model.copy() for model in ram_list]
        RamBlock.normalize_model(self.block_list)
        self.process_list = process_list
        self._first_cal()

    def _reset_special_para(self):
        pass

    def restart(self, ram_list, process_list):
        self.set_data(ram_list, process_list)
        self._reset_special_para()

        self.run()

    def run(self):
        self._clear_ram_bar()
        self._clear_process_bar()
        self._clear_temp_bar()
        self._clear_bottom_bar()
        self._clear_OV_bar()
        self.simulating = True
        self.cur_ram_index = 0
        self._end_ram_index = -1
        self.cur_free_ram_index = 0
        self.cur_free_ram: RamBlockDemo | None = None
        self.cur_process: ProcessDemo | None = None

        if len(self.block_list) != 0 and len(self.process_list) != 0:
            self._setup_rb_entries()
            self._setup_process_entries()

        self._end_ram_index = self.len_free_block - 1
        self._connect_timer(self._control_process_entry)

    def _first_cal(self):
        free_ram_size = [model.capacity for model in self.block_list if model.type_block == 0]
        process_size = [model.capacity for model in self.process_list]
        for p in range(len(self.process_list)):
            for r in range(len(free_ram_size)):
                if free_ram_size[r] >= process_size[p]:
                    free_ram_size[r] = free_ram_size[r] - process_size[p]
                    break
        self.min_ram_cap = min(free_ram_size)

    def _setup_rb_entries(self):
        RamBlock.update_block(self.block_list)
        self.min_pro_cap = Process.get_min(self.process_list).capacity

        self.len_process_list = len(self.process_list)

        self._height_list = []
        self.free_ram_block_wlist = []
        for model in self.block_list:
            rw = RamBlockDemo(model, self.min_ram_cap)
            if model.type_block == 0 or model.type_block == -1:
                self.free_ram_block_wlist.append(rw)
            self.mother.ui.ramBar_lo.addWidget(rw)
            self._height_list.append(rw.height())
        self.len_free_block = len(self.free_ram_block_wlist)

    def _setup_process_entries(self):
        Process.normalize_model(self.process_list)

        for model in self.process_list:
            rw = ProcessDemo(model, self.min_ram_cap)

            self.mother.ui.processBar_lo.addWidget(rw)

    def _reset_rb_entries(self):
        self._clear_ram_bar()
        self._setup_rb_entries()

    def _clear_ram_bar(self):
        for i in range(self.mother.ui.ramBar_lo.count()):
            self.mother.ui.ramBar_lo.itemAt(i).widget().deleteLater()

    def _clear_process_bar(self):
        for i in range(self.mother.ui.processBar_lo.count()):
            self.mother.ui.processBar_lo.itemAt(i).widget().deleteLater()

    def _clear_OV_bar(self):
        for i in range(self.mother.ui.processOVBar_lo.count()):
            self.mother.ui.processOVBar_lo.itemAt(i).widget().deleteLater()
        self.mother.ui.processOVBar_lo.addWidget(ProcessOVEntry('Tiên trình', 'Kích thước', 'Khối nhớ trống'))

    def _reset_process_entries(self):
        pass

    def set_time(self, t: int):
        self._speed = t
        self._merge_speed = round(self._speed*(2/3))

    def start(self, t: int | None = None):
        if t is not None:
            self.set_time(t)
            self._timer.start(t)
        pass

    def pause(self):
        self._timer.stop()

    def play(self):
        self._timer.start(self._speed)

    def _connect_timer(self, func, t: int | None = None):
        self._timer.timeout.disconnect()
        self._timer.timeout.connect(func)
        speed = t if t is not None else self._speed
        self._timer.start(speed)

    def _control_process_entry(self):
        if self.mother.ui.processBar_lo.count() == 0:
            self.simulating = False
            if self.mother.auto_run:
                self.mother.following_fit()
            else:
                self.mother.ui.pause_btn.setText("Chạy lại")
            self._timer.stop()

            return
        self._setup_cur_process()
        if self.len_free_block == 0:
            self.no_allocate(self.cur_process.model)
            self._connect_timer(self._control_process_entry)
            return
        # self._setup_cur_process()
        self._setup_cur_ram()
        self._connect_timer(self._decision)

    def no_allocate(self, process_model: Process):
        ui_model = ProcessDemo(process_model, self.min_ram_cap)
        self.mother.ui.bottomBar_lo.addWidget(ui_model)

        self._add_process_overview(process_model.index, process_model.capacity, 'Không được cấp')

        # Dọn tempBar
        self._clear_temp_bar()

    def _control_ram_entry(self):
        # Thiết lập khối ram hiện tại
        self.cur_free_ram_index = (self.cur_free_ram_index + 1) % self.len_free_block

        self._setup_cur_ram()
        # Quyết định cấp phát
        self._connect_timer(self._decision)

    def _setup_cur_ram(self):
        self.cur_free_ram = self.free_ram_block_wlist[self.cur_free_ram_index]
        self.cur_free_ram.high_light_effect()
        self._brick_stack(self.cur_free_ram.model.index)
        self.mother.ui.ramScrollArea.ensureWidgetVisible(self.cur_free_ram, yMargin=100)
        self.mother.ui.tempScrollArea.ensureWidgetVisible(self.cur_process, yMargin=100)


    def _setup_cur_process(self):
        temp = self.mother.ui.processBar_lo.itemAt(0).widget()
        self.mother.ui.processBar_lo.removeWidget(temp)
        self.cur_process = ProcessDemo(temp.model, temp.min_ram_cap)
        temp.deleteLater()
        self.mother.ui.tempBar_lo.addWidget(self.cur_process)
        if len(self.free_ram_block_wlist) > 0:
            self._brick_stack(self.free_ram_block_wlist[0].model.index)

    def _decision(self):
        self._normal_effect()
        if self.cur_free_ram.model.capacity >= self.cur_process.model.capacity:
            self.cur_free_ram.valid_effect()
            self._connect_timer(self._merge_action, self._merge_speed)
            self.cur_free_ram_index = 0
            return
        else:
            if self.cur_free_ram_index == self._end_ram_index:
                # self.cur_free_ram_index = 0
                # Đưa tiến trình khôngdđược cấp phát vào bottomBar
                self.no_allocate(self.cur_process.model)
                self.cur_free_ram_index = 0
                # Tiếp tục cấp phát cho tiến trình tiếp theo
                self._connect_timer(self._control_process_entry)
            else:
                self._connect_timer(self._control_ram_entry)

    def _merge_action(self):
        process_model = self.cur_process.model
        ram_model = self.cur_free_ram.model

        if ram_model.capacity < process_model.capacity:
            return
        self.block_list[ram_model.index] = RamBlock(ram_model.index, 2,
                                                    process_model.capacity)
        if process_model.capacity < ram_model.capacity:
            frag_model = RamBlock(-1, -1, ram_model.capacity - process_model.capacity)
            frag_model.free_index = ram_model.free_index
            RamBlock.insert_model(self.block_list, ram_model.index + 1, frag_model)

        self._add_process_overview(self.cur_process.model.index + 1, self.cur_process.model.capacity,
                                   self.cur_free_ram.model.free_index + 1)

        self.cur_process.deleteLater()
        self._reset_rb_entries()
        self._connect_timer(self._control_process_entry)

    def _add_process_overview(self, process_no: int, process_size: int, block_no: int):
        ov = ProcessOVEntry(process_no, process_size, block_no)
        self.mother.ui.processOVBar_lo.addWidget(ov)

    def _normal_effect(self):
        if self.cur_free_ram is not None:
            self.cur_free_ram.normal_effect()

    def kill_oj(self):
        self._timer.stop()
        self.deleteLater()

    def _clear_temp_bar(self):
        for i in range(self.mother.ui.tempBar_lo.count()):
            widget = self.mother.ui.tempBar_lo.itemAt(i).widget()
            widget.deleteLater()

    def _clear_bottom_bar(self):
        for i in range(self.mother.ui.bottomBar_lo.count()):
            widget = self.mother.ui.bottomBar_lo.itemAt(i).widget()
            widget.deleteLater()

    def _brick_stack(self, cur_rb_id: int):
        self.mother.ui.tempBar_lo.removeWidget(self.cur_process)
        if cur_rb_id > self.cur_ram_index:
            for i in range(self.cur_ram_index, cur_rb_id):
                model = self.block_list[i]
                temp_widget = RamBlockDemo(model, self.min_ram_cap, True)
                self.mother.ui.tempBar_lo.addWidget(temp_widget)
        elif cur_rb_id < self.cur_ram_index:
            self._clear_temp_bar()
            for i in range(0, cur_rb_id):
                model = self.block_list[i]
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
        self._normal_effect()
        if self.cur_free_ram.model.capacity >= self.cur_process.model.capacity:
            # Nếu khối nhớ vừa đủ với tiến trình thì khối nhớ bị đảy ra khỏi danh sách, cần cập nhật lại start index
            if self.cur_free_ram.model.capacity == self.cur_process.model.capacity and self.cur_free_ram_index == self.len_free_block - 1:
                self.cur_free_ram_index = 0
            # Thiết lập lại điểm kết thúc
            self._end_ram_index = (self.cur_free_ram_index - 1) % self.len_free_block
            self.cur_free_ram.valid_effect()
            self._connect_timer(self._merge_action, self._merge_speed)
        else:
            if self.cur_free_ram_index == self._end_ram_index:
                # Đưa tiến trình không được cấp phát vào bottomBar
                self.no_allocate(self.cur_process.model)
                self._end_ram_index = (self.cur_free_ram_index - 1) % self.len_free_block
                # Tiếp tục cấp phát cho tiến trình tiếp theo
                self._connect_timer(self._control_process_entry)
            else:
                self._connect_timer(self._control_ram_entry)


class BestFit(BaseFit):
    def __init__(self, mother_ui):
        super().__init__(mother_ui)
        self._min_block_id = -1

    def _get_best_block(self):
        return self.free_ram_block_wlist[self._min_block_id]

    def _first_cal(self):
        free_ram_size = [model.capacity for model in self.block_list if model.type_block == 0]
        process_size = [model.capacity for model in self.process_list]
        for p in range(len(self.process_list)):
            min_block_id = -1
            for r in range(len(free_ram_size)):
                if free_ram_size[r] >= process_size[p]:
                    if min_block_id==-1:
                        min_block_id = r
                    elif free_ram_size[r]<free_ram_size[min_block_id]:
                        min_block_id = r
            if min_block_id!=-1:
                free_ram_size[min_block_id] = free_ram_size[min_block_id] - process_size[p]
        self.min_ram_cap = min(free_ram_size)
        print(f'min: {self.min_ram_cap}')

    def _decision(self):
        self._normal_effect()
        if self.cur_free_ram.model.capacity >= self.cur_process.model.capacity:
            if self._min_block_id == -1:
                self._min_block_id = self.cur_free_ram_index
                self.cur_free_ram.valid_effect()

            elif self._get_best_block().model.capacity > self.cur_free_ram.model.capacity:
                self._get_best_block().normal_effect()
                self._min_block_id = self.cur_free_ram_index
                self.cur_free_ram.valid_effect()

        if self.cur_free_ram_index == self._end_ram_index:
            if self._min_block_id != -1:
                self.cur_free_ram = self._get_best_block()
                self._brick_stack(self.cur_free_ram.model.index)
                if self.cur_free_ram.model.capacity == self.cur_process.model.capacity:
                    self._end_ram_index -= 1
                self.cur_free_ram.valid_effect()
                self._connect_timer(self._merge_action, self._merge_speed)
                self._min_block_id = -1
            else:
                # Đưa tiến trình không được cấp phát vào bottomBar
                self.no_allocate(self.cur_process.model)
                self._connect_timer(self._control_process_entry)
            self.cur_free_ram_index = 0
            # Tiếp tục cấp phát cho tiến trình tiếp theo

        else:

            self._connect_timer(self._control_ram_entry)


class WorstFit(BaseFit):
    def __init__(self, mother_ui):
        super().__init__(mother_ui)
        self._max_block_id = -1

    def _decision(self):
        self._normal_effect()
        if self.cur_free_ram.model.capacity >= self.cur_process.model.capacity:
            if self._max_block_id == -1:
                self._max_block_id = self.cur_free_ram_index
                self.cur_free_ram.valid_effect()

            elif self.free_ram_block_wlist[self._max_block_id].model.capacity < self.cur_free_ram.model.capacity:
                self._max_block_id = self.cur_free_ram_index
                self.cur_free_ram.valid_effect()
        if self.cur_free_ram_index == self._end_ram_index:
            if self._max_block_id != -1:
                self.cur_free_ram = self.free_ram_block_wlist[self._max_block_id]
                self._brick_stack(self.cur_free_ram.model.index)
                if self.cur_free_ram.model.capacity == self.cur_process.model.capacity:
                    self._end_ram_index -= 1
                self._connect_timer(self._merge_action, self._merge_speed)
                self._max_block_id = -1
            else:
                # Đưa tiến trình không được cấp phát vào bottomBar
                self.no_allocate(self.cur_process.model)
                self._connect_timer(self._control_process_entry)
            self.cur_free_ram_index = 0
            # Tiếp tục cấp phát cho tiến trình tiếp theo

        else:
            self._connect_timer(self._control_ram_entry)
