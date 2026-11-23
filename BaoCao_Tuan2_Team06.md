# TRƯỜNG ĐẠI HỌC VĂN LANG
## KHOA CÔNG NGHỆ THÔNG TIN
---

# BÁO CÁO TIẾN ĐỘ ĐỒ ÁN NHÓM (TUẦN 2)
### MÔN HỌC: KIỂM THỬ TỰ ĐỘNG (KHÓA 27)

- **Đề tài**: Kiểm thử tự động ứng dụng Quản lý phân công giảng dạy
- **Phạm vi kiểm thử**: Các chức năng thuộc vai trò BCN Khoa (Faculty Board)
- **Lớp học phần**: `232_71ITSE41603_0102`
- **Nhóm thực hiện**: `Team 06`
  1. **Nguyễn Minh Phú** *(Nhóm trưởng)*
  2. **Trương Quốc Anh Khoa** *(Thành viên)*
  3. **Bùi Ngọc Thiệu** *(Thành viên)*
- **Thời gian báo cáo**: Tuần 2 - Tháng 10/2026

---

## PHẦN 1: KẾ HOẠCH THỰC HIỆN ĐỒ ÁN VÀ TIẾN ĐỘ TUẦN 1 - TUẦN 2

### 1.1. Mục tiêu và Kế hoạch tổng thể
Nhóm lập kế hoạch phân rã công việc (WBS) trong thời gian 8 tuần, làm việc 6 ngày/tuần (từ Thứ 2 đến Thứ 7), tập trung vào các chức năng của vai trò BCN Khoa.

### 1.2. Nhật ký tiến độ thực hiện chi tiết Tuần 1 và Tuần 2

| Tuần | Thứ | Nhiệm vụ cụ thể của từng thành viên | Sản phẩm bàn giao | Trạng thái |
|:---:|:---:|---|---|:---:|
| **Tuần 1** | **Thứ 2** | • **Nguyễn Minh Phú (NT)**: Họp nhóm kick-off, quán triệt đề bài FinalAssignment 1, tạo nhóm Zalo và Drive.<br>• **Trương Quốc Anh Khoa**: Tải và đọc tài liệu `ProductBacklog.xlsx`, `FunctionList_V1.8.xlsx`.<br>• **Bùi Ngọc Thiệu**: Tải và đọc tài liệu `UserGuide.pdf`, `Quy định tính thù lao.docx`. | Biên bản họp kick-off, Thư mục tài liệu chung | **Hoàn thành** |
| | **Thứ 3** | • **Nguyễn Minh Phú**: Phân tích cấu trúc thư mục nộp bài (`LopTH_Team#`) và quy chế nộp bài hàng tuần.<br>• **Trương Quốc Anh Khoa**: Lọc toàn bộ các chức năng của BCN Khoa từ FunctionList.<br>• **Bùi Ngọc Thiệu**: Đọc hiểu thuật ngữ chuyên môn trong phần mềm Quản lý phân công. | Bản tóm tắt quy định đề bài & Danh mục thuật ngữ | **Hoàn thành** |
| | **Thứ 4** | • **Nguyễn Minh Phú**: Phác thảo khung lịch biểu 8 tuần (6 ngày/tuần).<br>• **Trương Quốc Anh Khoa**: Xác định mốc bàn giao Test Cases và Automation Scripts.<br>• **Bùi Ngọc Thiệu**: Đóng góp ý kiến về phân bổ thời lượng các module. | Khung lịch biểu làm việc nhóm sơ bộ | **Hoàn thành** |
| | **Thứ 5** | • **Nguyễn Minh Phú**: Dự thảo file Word kế hoạch thực hiện đồ án nhóm.<br>• **Trương Quốc Anh Khoa**: Rà soát tính khả thi và phân công trách nhiệm 3 thành viên.<br>• **Bùi Ngọc Thiệu**: Chuẩn bị biểu mẫu nhật ký công việc (Work log). | Dự thảo bản kế hoạch công việc (.docx) | **Hoàn thành** |
| | **Thứ 6** | • **Nguyễn Minh Phú**: Hoàn thiện bảng kế hoạch đồ án nhóm chi tiết theo ngày.<br>• **Trương Quốc Anh Khoa**: Kiểm tra chéo phân công nhiệm vụ, đối chiếu yêu cầu đề bài.<br>• **Bùi Ngọc Thiệu**: Thiết lập kho mã nguồn chung trên Git/GitHub và Drive. | File kế hoạch hoàn chỉnh, Repo Git của nhóm | **Hoàn thành** |
| | **Thứ 7** | • **Cả nhóm (Phú, Khoa, Thiệu)**: Họp online tổng kết Tuần 1, duyệt kế hoạch và phân công Tuần 2. | Biên bản nghiệm thu Tuần 1 | **Hoàn thành** |
| **Tuần 2** | **Thứ 2** | • **Nguyễn Minh Phú**: Truy cập hệ thống website, kiểm tra quyền BCN Khoa.<br>• **Trương Quốc Anh Khoa**: Thử nghiệm luồng giao diện người dùng vai trò BCN Khoa.<br>• **Bùi Ngọc Thiệu**: Chụp màn hình trang chủ và thanh menu điều hướng BCN Khoa. | Hình ảnh giao diện trang chủ BCN Khoa | **Hoàn thành** |
| | **Thứ 3** | • **Nguyễn Minh Phú**: Khảo sát chi tiết Module Quản lý Người dùng (User Management).<br>• **Trương Quốc Anh Khoa**: Khảo sát chi tiết Module Quản lý Học kỳ (Term) và Ngành (Major).<br>• **Bùi Ngọc Thiệu**: Khảo sát chi tiết Module Thời khóa biểu (Import, Export, Phân công). | Ghi chú luồng hoạt động từng Module | **Hoàn thành** |
| | **Thứ 4** | • **Nguyễn Minh Phú**: Lập danh sách các phần tử HTML (ID, Name, XPath) của Module User.<br>• **Trương Quốc Anh Khoa**: Liệt kê các trường dữ liệu bắt buộc của Module Term và Major.<br>• **Bùi Ngọc Thiệu**: Khảo sát giao diện Thống kê và Bảng tính thù lao giảng dạy. | Bảng danh mục Element Locators sơ bộ | **Hoàn thành** |
| | **Thứ 5** | • **Nguyễn Minh Phú**: Phân loại các chức năng có thể tự động hóa vs kiểm thử thủ công.<br>• **Trương Quốc Anh Khoa**: Tổng hợp danh sách chức năng BCN Khoa đưa vào báo cáo Word.<br>• **Bùi Ngọc Thiệu**: Chụp toàn bộ ảnh giao diện từng chức năng BCN Khoa. | Bộ ảnh chụp màn hình UI đầy đủ của BCN Khoa | **Hoàn thành** |
| | **Thứ 6** | • **Nguyễn Minh Phú**: Soạn thảo nội dung Phần 1 & Phần 2 của Báo cáo đồ án Tuần 2.<br>• **Trương Quốc Anh Khoa**: Đối chiếu danh sách chức năng với Product Backlog để đảm bảo không sót.<br>• **Bùi Ngọc Thiệu**: Chèn và căn chỉnh hình ảnh chụp màn hình UI vào file Word. | Bản thảo Báo cáo đồ án Tuần 2 | **Hoàn thành** |
| | **Thứ 7** | • **Cả nhóm**: Họp online nghiệm thu kết quả khảo sát Tuần 2, hoàn thiện gói nộp bài Tuần 2. | Báo cáo Tuần 2 hoàn chỉnh (`Team06_Ver1.1.docx`) | **Hoàn thành** |

### 1.3. Đánh giá kết quả đạt được sau 2 tuần
- Tiến độ hoàn thành: **Đạt 100% kế hoạch**.
- Sản phẩm đầu ra: Kế hoạch WBS 8 tuần, danh sách chức năng BCN Khoa và trọn bộ ảnh chụp UI thực tế.

---

## PHẦN 2: KHẢO SÁT HỆ THỐNG VÀ PHẠM VI NGHIỆP VỤ BCN KHOA

### 2.1. Tổng quan hệ thống
- Hệ thống: **Quản lý phân công giảng dạy** (Khoa CNTT - Đại học Văn Lang).
- Địa chỉ: `https://cntttest.vanlanguni.edu.vn:18081/Phancong02/`.
- Nhóm người dùng: Ban chủ nhiệm Khoa (Faculty Board), Phụ trách bộ môn (Department Head), Giảng viên (Lecturer).

### 2.2. Phạm vi kiểm thử (Scope)
Nhóm chỉ thực hiện kiểm thử tự động cho vai trò **BCN Khoa (Faculty Board)** theo đúng yêu cầu của giảng viên.

---

## PHẦN 3: DANH SÁCH CHỨC NĂNG BCN KHOA CÓ THỂ TỰ ĐỘNG HÓA KIỂM THỬ

| STT | Mã CN | Tên chức năng | Mô tả nghiệp vụ | Độ ưu tiên | Khả năng Auto | Kịch bản test tự động đề xuất |
|:---:|:---:|---|---|:---:|:---:|---|
| 1 | `F.1.1` | Đăng nhập / Đăng xuất | Đăng nhập bằng email VLU quyền BCN Khoa và đăng xuất | High | **Có** | Kiểm thử login thành công, login sai mật khẩu, tài khoản không hợp lệ, logout. |
| 2 | `F.2.1` | Xem DS người dùng | Xem bảng danh sách người dùng, giảng viên trong hệ thống | Medium | **Có** | Kiểm thử tải bảng dữ liệu, phân trang, hiển thị đúng thông tin cột. |
| 3 | `F.2.2` | Thêm người dùng mới | Thêm giảng viên/người dùng mới kèm phân quyền trong Khoa | High | **Có** | Kiểm thử tạo user thành công, kiểm thử validation để trống, trùng mã GV/email. |
| 4 | `F.2.3` | Cập nhật người dùng | Chỉnh sửa thông tin cá nhân, phân quyền của người dùng | High | **Có** | Kiểm thử cập nhật họ tên, vai trò, số điện thoại, kiểm tra lưu thành công. |
| 5 | `F.2.4` | Xóa người dùng | Xóa tài khoản người dùng khỏi hệ thống | High | **Có** | Kiểm thử bấm xóa, xác nhận popup dialog confirm xóa, kiểm tra user biến mất. |
| 6 | `F.2.5` | Tìm kiếm người dùng | Tìm kiếm người dùng theo tên, mã giảng viên hoặc email | Medium | **Có** | Kiểm thử nhập từ khóa hợp lệ, từ khóa không tồn tại, kiểm tra kết quả lọc. |
| 7 | `F.2.6` | Khóa tài khoản | Khóa tài khoản giảng viên đã nghỉ hoặc chuyển công tác | Medium | **Có** | Kiểm thử đổi trạng thái Active sang Locked, xác nhận user không login được. |
| 8 | `F.3.1` | Xem danh sách học kỳ | Xem bảng tổng hợp các học kỳ trong năm | Medium | **Có** | Kiểm thử hiển thị danh sách học kỳ, kiểm tra thứ tự sắp xếp. |
| 9 | `F.3.2` | Tạo học kỳ mới | Tạo học kỳ mới (Mã HK, Tên HK, ngày bắt đầu, ngày kết thúc) | High | **Có** | Kiểm thử tạo HK hợp lệ, kiểm thử trùng mã HK, ngày kết thúc trước ngày bắt đầu. |
| 10 | `F.3.3` | Cập nhật học kỳ | Chỉnh sửa thông tin học kỳ đã tạo | High | **Có** | Kiểm thử sửa tên học kỳ, đổi ngày kết thúc, kiểm tra lưu thành công. |
| 11 | `F.3.4` | Xóa học kỳ | Xóa học kỳ chưa phát sinh dữ liệu thời khóa biểu | High | **Có** | Kiểm thử xóa học kỳ rác, kiểm tra thông báo không cho xóa nếu đã có TKB. |
| 12 | `F.3.5` | Tìm kiếm học kỳ | Tìm kiếm học kỳ theo tên hoặc mã | Medium | **Có** | Kiểm thử lọc học kỳ theo từ khóa năm học. |
| 13 | `F.3.6` | Khóa học kỳ | Khóa học kỳ để ngăn chặn chỉnh sửa sau khi đã chốt dữ liệu | High | **Có** | Kiểm thử khóa HK, verify các nút sửa/xóa TKB bị vô hiệu hóa. |
| 14 | `F.4.1-F.4.5` | Quản lý Ngành học | Xem danh sách, Thêm, Sửa, Xóa và Tìm kiếm ngành học | Medium | **Có** | Kiểm thử trọn bộ CRUD ngành học (CNTT, KTPM, MMT...), kiểm tra validation. |
| 15 | `F.5.1` | Import thời khóa biểu | Tải lên tệp Excel thời khóa biểu từ Phòng Đào tạo | High | **Có** | Kiểm thử upload tệp Excel chuẩn, tệp sai định dạng, tệp rỗng bằng sendKeys. |
| 16 | `F.5.2` | Export thời khóa biểu | Xuất file Excel TKB đã phân công để gửi Phòng Đào tạo | High | **Có** | Kiểm thử nhấp nút Export, verify tệp Excel được tải về thư mục Downloads. |
| 17 | `F.5.3` | Xem TKB toàn khoa | Xem bảng TKB toàn khoa theo tuần và theo giảng viên | Medium | **Có** | Kiểm thử lọc theo tuần, chuyển đổi giữa chế độ xem tuần và học kỳ. |
| 18 | `F.5.4` | Phân công giảng viên | Chọn giảng viên phụ trách cho từng lớp học phần trên TKB | High | **Có** | Kiểm thử chọn giảng viên từ Dropdown, kiểm tra cảnh báo trùng lịch dạy. |
| 19 | `F.5.5` | Xóa lớp học phần | Xóa lớp học phần thừa hoặc bị hủy trên TKB | Medium | **Có** | Kiểm thử xóa lớp HP, kiểm tra lớp biến mất khỏi bảng TKB. |
| 20 | `F.6.1-F.6.3` | Quản lý Thống kê | Thống kê số giờ dạy, số môn dạy theo học kỳ và năm | Medium | **Có** | Kiểm thử bộ lọc học kỳ, kiểm tra số liệu tổng giờ dạy hiển thị đúng. |
| 21 | `F.7.1-F.7.19` | Quản lý Thù lao | Quản lý học hàm, học vị, hệ số thù lao và bảng tính tiền dạy | Low | **Có** | Kiểm thử cập nhật hệ số thù lao, xem bảng tính lương giảng dạy theo công thức. |

---

## PHẦN 4: HÌNH ẢNH GIAO DIỆN CÁC CHỨC NĂNG BCN KHOA (UI SCREENSHOTS)
*(Toàn bộ 8 hình ảnh giao diện thực tế đã được nhúng trực tiếp vào file Word [Team06_Ver1.1.docx](file:///D:/ktdt/Do%20an%20nhom/Team06_Ver1.1.docx))*:
- **Hình 1**: Giao diện Trang chủ và Đăng nhập hệ thống bằng email VLU (`F.1.1`).
- **Hình 2**: Giao diện Danh sách Người dùng trong Khoa (`F.2.1`).
- **Hình 3**: Giao diện Quản lý Học kỳ (`F.3.1`).
- **Hình 4**: Giao diện Form Thêm mới Học kỳ (`F.3.2`).
- **Hình 5**: Giao diện Quản lý Ngành học (`F.4.1`).
- **Hình 6**: Giao diện Bảng Thời khóa biểu và Phân công giảng viên (`F.5.3` & `F.5.4`).
- **Hình 7**: Giao diện Thống kê số giờ dạy theo học kỳ (`F.6.1`).
- **Hình 8**: Giao diện Quản lý Bảng tính Thù lao giảng dạy (`F.7.19`).

---

## PHẦN 5: KẾ HOẠCH TRIỂN KHAI CHO TUẦN 3
1. **Nguyễn Minh Phú (Nhóm trưởng)**: Định hình cấu trúc mẫu Test Case chuẩn IEEE 829; review và chuẩn hóa bộ Test Cases cho Module Đăng nhập & Người dùng.
2. **Trương Quốc Anh Khoa**: Thiết kế chi tiết Test Cases cho chức năng Đăng nhập (`F.1.1`) và Quản lý Người dùng (`F.2.1` – `F.2.4`).
3. **Bùi Ngọc Thiệu**: Thiết kế Test Cases cho chức năng Tìm kiếm (`F.2.5`), Khóa tài khoản (`F.2.6`); chuẩn bị bộ dữ liệu kiểm thử (Test Data).
4. **Cả nhóm**: Họp nghiệm thu vào tối Thứ 7 của Tuần 3 để chốt danh sách Test Cases chuyển giao sang giai đoạn lập trình tự động hóa.
