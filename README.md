# Mô Phỏng Các Thuật Toán Cấp Phát Bộ Nhớ

## Giới thiệu
Ứng dụng mô phỏng trực quan các thuật toán cấp phát bộ nhớ trong hệ điều hành, được phát triển bằng Python và PyQt5. Dự án này giúp người dùng hiểu rõ cách thức hoạt động của các thuật toán quản lý bộ nhớ thông qua giao diện đồ họa sinh động.

## Demo Video
🎬 **Xem video chạy thử nghiệm chương trình:**

[![Video Demo](video%20ch%E1%BA%A1y%20th%E1%BB%AD%20nghi%E1%BB%87m%20ch%C6%B0%C6%A1ng%20tr%C3%ACnh.gif)

*Click vào badge trên để xem video demo chi tiết các tính năng của ứng dụng*

## Chức năng chính

### 🎯 Các thuật toán được hỗ trợ:
- **First Fit** - Cấp phát khối nhớ trống đầu tiên phù hợp
- **Next Fit** - Cấp phát từ vị trí cuối cùng được sử dụng
- **Best Fit** - Cấp phát khối nhớ nhỏ nhất phù hợp
- **Worst Fit** - Cấp phát khối nhớ lớn nhất có sẵn

### 🖥️ Giao diện mô phỏng:
- Hiển thị trực quan các khối nhớ RAM với màu sắc phân biệt trạng thái
- Hiển thị danh sách tiến trình chờ cấp phát
- Theo dõi quá trình phân mảnh bộ nhớ
- Điều khiển tốc độ mô phỏng (x0.75, x1, x1.25)
- Chế độ tự động chạy hoặc thực hiện từng bước

### 📊 Ý nghĩa màu sắc khối nhớ:
- 🟢 **Khối nhớ trống** (màu xanh lá) - Sẵn sàng cấp phát
- 🔴 **Khối nhớ đã sử dụng** (màu đỏ) - Đã được tiến trình chiếm dụng
- 🔵 **Khối nhớ được cấp phát** (màu xanh dương) - Vừa được cấp cho tiến trình
- 🟣 **Khối nhớ bị phân mảnh** (màu tím) - Kết quả của việc phân mảnh

## Cấu trúc dự án
```
├── Views/              # Giao diện người dùng (PyQt5 UI)
│   ├── MainUI.py      # Giao diện chính
│   ├── DemoFrame.py   # Khung mô phỏng
│   └── *.ui           # File thiết kế giao diện
├── Controller/         # Logic xử lý và thuật toán
│   ├── Models.py      # Định nghĩa RamBlock và Process
│   ├── fitController.py # Các thuật toán cấp phát
│   └── siController.py # Điều khiển mô phỏng
└── main.py            # File chạy chính
```

## Yêu cầu hệ thống
- Python 3.x
- PyQt5
- Các thư viện Python cơ bản

## Hướng dẫn cài đặt và sử dụng

### 1. Clone repository
```bash
git clone https://github.com/dait17/Simulating-RAM-MAP.git
cd Simulating-RAM-MAP
```

### 2. Cài đặt thư viện
```bash
pip install PyQt5
```

### 3. Chạy ứng dụng
```bash
python main.py
```

### 4. Sử dụng ứng dụng
1. Nhập thông tin khối nhớ và tiến trình
2. Chọn thuật toán cấp phát mong muốn
3. Điều chỉnh tốc độ mô phỏng
4. Bắt đầu mô phỏng và quan sát quá trình

## Mục đích sử dụng
- 📚 **Giáo dục:** Hỗ trợ việc giảng dạy và học tập môn Hệ điều hành
- 🔬 **Nghiên cứu:** So sánh hiệu quả của các thuật toán cấp phát bộ nhớ
- 🎓 **Thực hành:** Giúp sinh viên hiểu rõ lý thuyết thông qua thực hành trực quan

## Tác giả
Phát triển bởi **dait17** - Dự án thực tập cơ sở

---
*💡 Dự án này nhằm mục đích giáo dục, giúp sinh viên và người học hiểu rõ hơn về các thuật toán quản lý bộ nhớ trong hệ điều hành thông qua mô phỏng trực quan.*
