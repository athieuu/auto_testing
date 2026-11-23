import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()

# Setup sheets
ws_info = wb.active
ws_info.title = "1. Thông tin chung"
ws_schedule = wb.create_sheet(title="2. Lịch biểu chi tiết (WBS)")
ws_summary = wb.create_sheet(title="3. Tổng hợp tiến độ")

# Fonts & Fills
font_title = Font(name="Times New Roman", size=16, bold=True, color="003366")
font_subtitle = Font(name="Times New Roman", size=12, italic=True)
font_sec_hdr = Font(name="Times New Roman", size=13, bold=True, color="003366")
font_tbl_hdr = Font(name="Times New Roman", size=11, bold=True, color="FFFFFF")
font_data = Font(name="Times New Roman", size=10)
font_data_bold = Font(name="Times New Roman", size=10, bold=True)

fill_hdr = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
fill_subhdr = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
fill_zebra = PatternFill(start_color="F2F5F8", end_color="F2F5F8", fill_type="solid")
fill_done = PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid") # light green
font_done = Font(name="Times New Roman", size=10, bold=True, color="375623")

thin_border_side = Side(border_style="thin", color="D9D9D9")
thin_border = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)
thick_bottom = Border(bottom=Side(border_style="medium", color="003366"))

# ========================================================
# SHEET 1: THÔNG TIN CHUNG
# ========================================================
ws_info.views.sheetView[0].showGridLines = True
ws_info['A1'] = "TRƯỜNG ĐẠI HỌC VĂN LANG - KHOA CÔNG NGHỆ THÔNG TIN"
ws_info['A1'].font = Font(name="Times New Roman", size=12, bold=True)
ws_info['A2'] = "KẾ HOẠCH THỰC HIỆN ĐỒ ÁN NHÓM - KIỂM THỬ TỰ ĐỘNG"
ws_info['A2'].font = font_title
ws_info['A3'] = "Đề tài: Kiểm thử tự động ứng dụng Quản lý phân công giảng dạy (Vai trò: BCN Khoa)"
ws_info['A3'].font = font_subtitle

ws_info['A5'] = "1. THÔNG TIN DỰ ÁN & LỚP HỌC PHẦN"
ws_info['A5'].font = font_sec_hdr

info_rows = [
    ("Tên môn học:", "Kiểm thử tự động (Software Automation Testing)"),
    ("Mã lớp học phần:", "232_71ITSE41603_0102"),
    ("Tên nhóm thực hiện:", "Team 06"),
    ("Số lượng thành viên:", "03 sinh viên"),
    ("Hệ thống kiểm thử:", "https://cntttest.vanlanguni.edu.vn:18081/Phancong02/"),
    ("Phạm vi kiểm thử:", "Chỉ kiểm thử các chức năng của vai trò BCN Khoa (Faculty Board)"),
    ("Chế độ làm việc:", "6 ngày/tuần (Thứ 2 đến Thứ 7) trong 8 tuần (Tổng cộng 48 ngày làm việc)")
]

for idx, (label, val) in enumerate(info_rows, start=6):
    ws_info.cell(row=idx, column=1, value=label).font = font_data_bold
    ws_info.cell(row=idx, column=2, value=val).font = font_data

ws_info['A14'] = "2. DANH SÁCH THÀNH VIÊN VÀ PHÂN CÔNG VAI TRÒ"
ws_info['A14'].font = font_sec_hdr

member_headers = ["STT", "Họ và tên", "Vai trò trong nhóm", "Trách nhiệm & Nhiệm vụ chính phụ trách"]
for col_idx, h in enumerate(member_headers, start=1):
    c = ws_info.cell(row=15, column=col_idx, value=h)
    c.font = font_tbl_hdr
    c.fill = fill_hdr
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

members = [
    (1, "Nguyễn Minh Phú", "Nhóm trưởng (Team Leader)", 
     "• Quản lý tiến độ chung của nhóm, phân chia công việc hằng ngày.\n"
     "• Khởi tạo kiến trúc dự án (Maven, Selenium 4, TestNG, Surefire Plugin).\n"
     "• Tự động hóa Module Đăng nhập (F.1.1) & Quản lý Người dùng (F.2.1 - F.2.6).\n"
     "• Tích hợp test suite vào testng.xml, tối ưu mã nguồn và nộp bài lên E-learning."),
    (2, "Trương Quốc Anh Khoa", "Thành viên (Tester / Dev)", 
     "• Khảo sát hệ thống thực tế tại website, lọc danh mục chức năng BCN Khoa.\n"
     "• Thiết kế bộ kịch bản kiểm thử (Test Cases) chi tiết cho toàn bộ các module.\n"
     "• Tự động hóa Module Quản lý Học kỳ (F.3.1 - F.3.6) & Quản lý Ngành (F.4.1 - F.4.5).\n"
     "• Chuẩn hóa dữ liệu test và tối ưu các bộ chọn XPath/CSS Locators."),
    (3, "Bùi Ngọc Thiệu", "Thành viên (Tester / Document)", 
     "• Nghiên cứu tài liệu quy định tính thù lao giảng dạy và định mức giờ dạy.\n"
     "• Tự động hóa Module Quản lý Thời khóa biểu (F.5.1 - F.5.6) & Thù lao (F.7).\n"
     "• Chụp ảnh giao diện minh họa các chức năng BCN Khoa.\n"
     "• Soạn thảo báo cáo Word Team06_Ver1.0.docx và đóng gói file mã nguồn Team06_Ver1.0.zip.")
]

for row_idx, m in enumerate(members, start=16):
    ws_info.cell(row=row_idx, column=1, value=m[0]).alignment = Alignment(horizontal="center", vertical="top")
    ws_info.cell(row=row_idx, column=2, value=m[1]).font = font_data_bold
    ws_info.cell(row=row_idx, column=2).alignment = Alignment(vertical="top")
    ws_info.cell(row=row_idx, column=3, value=m[2]).alignment = Alignment(vertical="top")
    ws_info.cell(row=row_idx, column=4, value=m[3]).alignment = Alignment(vertical="top", wrap_text=True)
    for c_i in range(1, 5):
        cell = ws_info.cell(row=row_idx, column=c_i)
        cell.font = font_data if c_i != 2 else font_data_bold
        cell.border = thin_border

ws_info.column_dimensions['A'].width = 8
ws_info.column_dimensions['B'].width = 24
ws_info.column_dimensions['C'].width = 28
ws_info.column_dimensions['D'].width = 80

# ========================================================
# SHEET 2: LỊCH BIỂU CHI TIẾT TỪNG NGÀY (48 NGÀY)
# ========================================================
ws_schedule.views.sheetView[0].showGridLines = True
ws_schedule['A1'] = "BẢNG LỊCH BIỂU CÔNG VIỆC CHI TIẾT ĐỒ ÁN NHÓM - TEAM 06"
ws_schedule['A1'].font = font_title
ws_schedule['A2'] = "Làm việc 6 ngày/tuần (từ Thứ 2 đến Thứ 7) - Phân công chi tiết cho 3 thành viên"
ws_schedule['A2'].font = font_subtitle

sched_headers = [
    "STT", "Tuần", "Thứ", "Giai đoạn", 
    "Nhiệm vụ: Nguyễn Minh Phú (NT)", 
    "Nhiệm vụ: Trương Quốc Anh Khoa", 
    "Nhiệm vụ: Bùi Ngọc Thiệu", 
    "Sản phẩm bàn giao (Deliverable)", 
    "Trạng thái"
]

for col_idx, h in enumerate(sched_headers, start=1):
    c = ws_schedule.cell(row=4, column=col_idx, value=h)
    c.font = font_tbl_hdr
    c.fill = fill_hdr
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
ws_schedule.row_dimensions[4].height = 28

daily_data = [
    # TUAN 1
    (1, "Tuần 1", "Thứ 2", "1. Khởi động",
     "Họp nhóm kick-off, quán triệt đề bài FinalAssignment 1, tạo nhóm Zalo và Google Drive.",
     "Tải và đọc tài liệu ProductBacklog.xlsx, FunctionList_V1.8.xlsx.",
     "Tải và đọc tài liệu UserGuide.pdf, Quy định tính thù lao.docx.",
     "Biên bản họp kick-off, Thư mục lưu trữ chung", "Hoàn thành"),
    (2, "Tuần 1", "Thứ 3", "1. Khởi động",
     "Phân tích cấu trúc thư mục nộp bài (LopTH_Team#) và quy định nộp bài hàng tuần.",
     "Lọc toàn bộ các chức năng thuộc vai trò BCN Khoa từ FunctionList.",
     "Đọc hiểu các thuật ngữ chuyên môn trong phần mềm Quản lý phân công giảng dạy.",
     "Bản tóm tắt quy định đề bài & Danh mục thuật ngữ", "Hoàn thành"),
    (3, "Tuần 1", "Thứ 4", "1. Khởi động",
     "Phác thảo khung lịch biểu 8 tuần làm việc (6 ngày/tuần).",
     "Xác định các mốc bàn giao Test Cases và Automation Scripts.",
     "Đóng góp ý kiến về thời lượng từng module kiểm thử.",
     "Khung lịch biểu làm việc nhóm sơ bộ", "Hoàn thành"),
    (4, "Tuần 1", "Thứ 5", "1. Khởi động",
     "Dự thảo file Word kế hoạch thực hiện đồ án nhóm.",
     "Rà soát tính khả thi và phân công trách nhiệm từng thành viên.",
     "Chuẩn bị biểu mẫu nhật ký công việc (Work log).",
     "Dự thảo bản kế hoạch công việc (.docx)", "Hoàn thành"),
    (5, "Tuần 1", "Thứ 6", "1. Khởi động",
     "Hoàn thiện bảng kế hoạch đồ án nhóm chi tiết theo ngày.",
     "Kiểm tra chéo phân công nhiệm vụ, đối chiếu yêu cầu đề bài.",
     "Thiết lập kho mã nguồn chung trên Git/GitHub và Drive.",
     "File kế hoạch hoàn chỉnh, Repo Git của nhóm", "Hoàn thành"),
    (6, "Tuần 1", "Thứ 7", "1. Khởi động",
     "Họp online tổng kết Tuần 1, phân công nhiệm vụ Tuần 2.",
     "Tham gia họp online, tiếp nhận nhiệm vụ Tuần 2.",
     "Ghi biên bản họp Tuần 1, lập danh sách việc cần làm Tuần 2.",
     "Biên bản nghiệm thu Tuần 1", "Hoàn thành"),

    # TUAN 2
    (7, "Tuần 2", "Thứ 2", "2. Khảo sát UI",
     "Truy cập hệ thống website, kiểm tra quyền BCN Khoa.",
     "Thử nghiệm luồng giao diện người dùng vai trò BCN Khoa.",
     "Chụp màn hình trang chủ và thanh menu điều hướng BCN Khoa.",
     "Hình ảnh giao diện trang chủ BCN Khoa", "Hoàn thành"),
    (8, "Tuần 2", "Thứ 3", "2. Khảo sát UI",
     "Khảo sát chi tiết Module Quản lý Người dùng (User Management).",
     "Khảo sát chi tiết Module Quản lý Học kỳ (Term) và Ngành (Major).",
     "Khảo sát chi tiết Module Thời khóa biểu (Import, Export, Phân công).",
     "Ghi chú luồng hoạt động từng Module", "Hoàn thành"),
    (9, "Tuần 2", "Thứ 4", "2. Khảo sát UI",
     "Lập danh sách các phần tử HTML (ID, Name, XPath) của Module User.",
     "Liệt kê các trường dữ liệu bắt buộc của Module Term và Major.",
     "Khảo sát giao diện Thống kê và Bảng tính thù lao giảng dạy.",
     "Bảng danh mục Element Locators sơ bộ", "Hoàn thành"),
    (10, "Tuần 2", "Thứ 5", "2. Khảo sát UI",
     "Phân loại các chức năng có thể tự động hóa vs thủ công.",
     "Tổng hợp danh sách chức năng BCN Khoa đưa vào báo cáo Word.",
     "Chụp toàn bộ ảnh giao diện từng chức năng BCN Khoa.",
     "Bộ ảnh chụp màn hình UI đầy đủ của BCN Khoa", "Hoàn thành"),
    (11, "Tuần 2", "Thứ 6", "2. Khảo sát UI",
     "Soạn thảo nội dung phần 1 của file báo cáo Word (Danh sách chức năng BCN Khoa).",
     "Đối chiếu danh sách chức năng với Product Backlog để đảm bảo không sót.",
     "Chèn và căn chỉnh hình ảnh chụp màn hình vào file Word.",
     "Bản thảo báo cáo phần Danh sách chức năng BCN Khoa", "Hoàn thành"),
    (12, "Tuần 2", "Thứ 7", "2. Khảo sát UI",
     "Họp online nghiệm thu kết quả khảo sát Tuần 2.",
     "Báo cáo danh mục chức năng đã hoàn thành.",
     "Ghi biên bản họp Tuần 2, chuẩn bị thiết kế Test Cases.",
     "Biên bản họp nghiệm thu Tuần 2", "Hoàn thành"),

    # TUAN 3
    (13, "Tuần 3", "Thứ 2", "3. Thiết kế TC",
     "Thống nhất cấu trúc template Test Case Excel.",
     "Viết kịch bản kiểm thử chức năng Đăng nhập F.1.1 (hợp lệ, sai pass, bỏ trống).",
     "Chuẩn bị danh sách tài khoản kiểm thử (Test Accounts BCN Khoa).",
     "File Test Cases Module Đăng nhập (Excel)", "Hoàn thành"),
    (14, "Tuần 3", "Thứ 3", "3. Thiết kế TC",
     "Hướng dẫn kỹ thuật phân vùng tương đương và giá trị biên cho form Thêm người dùng.",
     "Thiết kế Test Cases cho F.2.1 (Xem DS) và F.2.2 (Thêm mới người dùng).",
     "Chuẩn bị dữ liệu kiểm thử người dùng (Mã GV, Tên, Email VLU).",
     "Test Cases Thêm mới người dùng", "Hoàn thành"),
    (15, "Tuần 3", "Thứ 4", "3. Thiết kế TC",
     "Review Test Cases Thêm mới người dùng, bổ sung case trùng mã GV/email.",
     "Thiết kế Test Cases cho F.2.3 (Cập nhật) và F.2.4 (Xóa người dùng).",
     "Thiết kế Test Cases cho F.2.5 (Tìm kiếm) và F.2.6 (Khóa tài khoản).",
     "Test Cases Cập nhật, Xóa, Tìm kiếm, Khóa user", "Hoàn thành"),
    (16, "Tuần 3", "Thứ 5", "3. Thiết kế TC",
     "Thiết kế các Test Cases kiểm thử biên cho trường Mã GV và định dạng Email.",
     "Bổ sung các kịch bản kiểm tra thông báo lỗi validation trên giao diện.",
     "Tổng hợp bảng Test Data hoàn chỉnh vào Excel.",
     "Bộ dữ liệu Test Data chuẩn cho Module 1", "Hoàn thành"),
    (17, "Tuần 3", "Thứ 6", "3. Thiết kế TC",
     "Rà soát toàn diện bộ Test Cases Module Login & User Management.",
     "Chuẩn hóa mã định danh Test Case (TC_LOGIN_xx, TC_USER_xx).",
     "Cập nhật nội dung bảng Test Cases vào file Word báo cáo.",
     "Tài liệu Test Cases Module 1 hoàn chỉnh", "Hoàn thành"),
    (18, "Tuần 3", "Thứ 7", "3. Thiết kế TC",
     "Họp nghiệm thu bộ Test Cases Module 1, đánh giá độ bao phủ.",
     "Báo cáo số lượng Test Cases Module Login & User.",
     "Ghi biên bản họp Tuần 3, giao việc thiết kế Module 2.",
     "Biên bản nghiệm thu Tuần 3", "Hoàn thành"),

    # TUAN 4
    (19, "Tuần 4", "Thứ 2", "3. Thiết kế TC",
     "Phân tích quy tắc nghiệp vụ Module Quản lý Học kỳ (F.3).",
     "Viết Test Cases cho F.3.1 (Xem DS), F.3.2 (Tạo mới), F.3.3 (Cập nhật HK).",
     "Viết Test Cases cho F.3.4 (Xóa HK), F.3.5 (Tìm kiếm), F.3.6 (Khóa học kỳ).",
     "Test Cases Module Quản lý Học kỳ", "Hoàn thành"),
    (20, "Tuần 4", "Thứ 3", "3. Thiết kế TC",
     "Thiết kế Test Cases cho Module Quản lý Ngành (F.4.1 - F.4.5).",
     "Chuẩn bị dữ liệu kiểm thử ngành học (Mã ngành, tên ngành).",
     "Nghiên cứu cấu trúc tệp Excel thời khóa biểu chuẩn dùng để Import.",
     "Test Cases Module Quản lý Ngành", "Hoàn thành"),
    (21, "Tuần 4", "Thứ 4", "3. Thiết kế TC",
     "Thiết kế Test Cases cho F.5.1 (Import TKB: hợp lệ, sai định dạng, file trống).",
     "Thiết kế Test Cases cho F.5.2 (Export TKB) và F.5.3 (Xem TKB toàn khoa).",
     "Thiết kế Test Cases cho F.5.4 (Phân công GV) và F.5.5 (Xóa lớp HP).",
     "Test Cases Import/Export và Phân công TKB", "Hoàn thành"),
    (22, "Tuần 4", "Thứ 5", "3. Thiết kế TC",
     "Thiết kế Test Cases cho Module Thống kê (F.6) và Thù lao (F.7).",
     "Bổ sung kịch bản kiểm tra logic tính giờ theo công thức quy định.",
     "Tạo tệp Excel TKB thử nghiệm mẫu chứa các lớp học phần phục vụ test.",
     "Tệp Excel TKB test mẫu", "Hoàn thành"),
    (23, "Tuần 4", "Thứ 6", "3. Thiết kế TC",
     "Rà soát ma trận truy xuất nguồn gốc (Traceability Matrix).",
     "Đồng bộ hóa toàn bộ mã định danh Test Case (TC_TERM_xx, TC_TKB_xx).",
     "Tổng hợp toàn bộ Test Cases giai đoạn 2 vào file Word báo cáo.",
     "Tài liệu đặc tả Test Cases toàn hệ thống", "Hoàn thành"),
    (24, "Tuần 4", "Thứ 7", "3. Thiết kế TC",
     "Họp tổng kết giai đoạn Thiết kế Test Cases, thống nhất phương án Automation.",
     "Báo cáo hoàn thành 100% Test Cases thiết kế.",
     "Ghi biên bản họp Tuần 4, chuẩn bị dựng Base Framework.",
     "Biên bản chốt danh sách Test Case tự động hóa", "Hoàn thành"),

    # TUAN 5
    (25, "Tuần 5", "Thứ 2", "4. Lập trình Auto",
     "Khởi tạo Maven Project, cấu hình pom.xml (Selenium 4.25, TestNG 7.10, Surefire).",
     "Viết lớp BasePage.java xử lý Explicit Wait, Click, SendKeys.",
     "Viết lớp BaseTest.java quản lý vòng đời ChromeDriver, Timeouts, Window Maximize.",
     "Base Framework POM hoàn chỉnh", "Hoàn thành"),
    (26, "Tuần 5", "Thứ 3", "4. Lập trình Auto",
     "Xây dựng LoginPage.java (locators và phương thức login, logout).",
     "Viết test class LoginTest.java với các test case đăng nhập hợp lệ/không hợp lệ.",
     "Chạy thử nghiệm LoginTest, kiểm tra tính ổn định trên Chrome.",
     "Mã nguồn LoginPage.java và LoginTest.java", "Hoàn thành"),
    (27, "Tuần 5", "Thứ 4", "4. Lập trình Auto",
     "Xây dựng UserManagementPage.java (bảng người dùng, form thêm/sửa/xóa).",
     "Viết test method kiểm tra Xem danh sách và Tìm kiếm người dùng.",
     "Viết test method Thêm mới người dùng với assertion thông báo thành công.",
     "Mã nguồn UserManagementPage.java", "Hoàn thành"),
    (28, "Tuần 5", "Thứ 5", "4. Lập trình Auto",
     "Viết kịch bản tự động Cập nhật thông tin và Xóa người dùng.",
     "Áp dụng @DataProvider kiểm thử form User với nhiều tập dữ liệu.",
     "Viết kịch bản tự động kiểm thử chức năng Khóa tài khoản giảng viên.",
     "Mã nguồn UserManagementTest.java", "Hoàn thành"),
    (29, "Tuần 5", "Thứ 6", "4. Lập trình Auto",
     "Tối ưu mã nguồn Module 1, push code lên Git repo chung.",
     "Đo thời gian chạy của test case và điều chỉnh wait hợp lý.",
     "Viết tài liệu giải thích source code Module Login & User vào file báo cáo Word.",
     "Báo cáo giải thích source code Module 1", "Hoàn thành"),
    (30, "Tuần 5", "Thứ 7", "4. Lập trình Auto",
     "Họp review mã nguồn Module 1, chạy kiểm thử xác nhận tất cả test case Pass.",
     "Demo chạy LoginTest và UserManagementTest.",
     "Ghi biên bản họp Tuần 5, phân công Module 2.",
     "Biên bản nghiệm thu mã nguồn Tuần 5", "Hoàn thành"),

    # TUAN 6
    (31, "Tuần 6", "Thứ 2", "4. Lập trình Auto",
     "Thiết kế kiến trúc Page Object cho Module Quản lý Học kỳ và Ngành.",
     "Xây dựng TermManagementPage.java và TermManagementTest.java.",
     "Xây dựng MajorManagementPage.java và MajorManagementTest.java.",
     "Page Objects cho Học kỳ và Ngành", "Hoàn thành"),
    (32, "Tuần 6", "Thứ 3", "4. Lập trình Auto",
     "Kiểm tra tính độc lập và xử lý dữ liệu động cho TermManagementTest.",
     "Hoàn thiện kịch bản Tạo học kỳ mới (F.3.2) và Khóa học kỳ (F.3.6).",
     "Hoàn thiện kịch bản Thêm, Sửa, Xóa ngành học (F.4.1 - F.4.4).",
     "Mã nguồn TermManagementTest.java", "Hoàn thành"),
    (33, "Tuần 6", "Thứ 4", "4. Lập trình Auto",
     "Xây dựng TimetableManagementPage.java xử lý upload tệp và thao tác bảng TKB.",
     "Viết kịch bản tự động kiểm thử chức năng Import TKB từ tệp Excel (F.5.1).",
     "Viết kịch bản tự động kiểm thử chức năng Export TKB (F.5.2) và Xem TKB (F.5.3).",
     "Mã nguồn TimetableManagementPage.java", "Hoàn thành"),
    (34, "Tuần 6", "Thứ 5", "4. Lập trình Auto",
     "Viết kịch bản tự động Phân công giảng viên vào lớp học phần (F.5.4).",
     "Viết kịch bản tự động Xóa lớp học phần trên thời khóa biểu (F.5.5).",
     "Viết kịch bản kiểm thử Xem thời khóa biểu cá nhân của BCN Khoa (F.5.6).",
     "Mã nguồn TimetableManagementTest.java", "Hoàn thành"),
    (35, "Tuần 6", "Thứ 6", "4. Lập trình Auto",
     "Bổ sung xử lý ngoại lệ (Exception Handling) khi mạng lag hoặc trang load chậm.",
     "Chạy kiểm thử tự động toàn bộ Module 2 trên Chrome browser.",
     "Cập nhật source code và giải thích chi tiết Module 2 vào file Word báo cáo.",
     "Báo cáo giải thích source code Module 2", "Hoàn thành"),
    (36, "Tuần 6", "Thứ 7", "4. Lập trình Auto",
     "Họp nghiệm thu mã nguồn Module 2, tổng hợp log.",
     "Demo chạy kiểm thử Module Học kỳ và TKB.",
     "Ghi biên bản họp Tuần 6, chuẩn bị tích hợp Test Suite.",
     "Biên bản nghiệm thu Tuần 6", "Hoàn thành"),

    # TUAN 7
    (37, "Tuần 7", "Thứ 2", "5. Test Suite & Đo lường",
     "Xây dựng StatisticsPage.java và RemunerationPage.java.",
     "Viết kịch bản kiểm thử Thống kê giờ dạy theo học kỳ và năm (F.6.1 - F.6.2).",
     "Viết kịch bản kiểm thử Bảng tính thù lao giảng dạy (F.7.19).",
     "Mã nguồn StatisticsPage & RemunerationPage", "Hoàn thành"),
    (38, "Tuần 7", "Thứ 3", "5. Test Suite & Đo lường",
     "Tạo file testng.xml cấu hình toàn bộ Suite kiểm thử của vai trò BCN Khoa.",
     "Thiết lập độ ưu tiên (priority) và phụ thuộc giữa các test class.",
     "Viết file run_tests.bat hỗ trợ chạy kiểm thử 1-click không cần IDE.",
     "File testng.xml và run_tests.bat", "Hoàn thành"),
    (39, "Tuần 7", "Thứ 4", "5. Test Suite & Đo lường",
     "Thực thi toàn bộ Test Suite bằng lệnh Maven Surefire test.",
     "Ghi nhận kết quả thực thi (Pass rate, Fail rate, lỗi phát sinh).",
     "Chụp ảnh kết quả TestNG Report và Console output.",
     "Surefire Report & TestNG HTML Report", "Hoàn thành"),
    (40, "Tuần 7", "Thứ 5", "5. Test Suite & Đo lường",
     "Phân tích các trường hợp fail, sửa lỗi assertion và tối ưu timeout.",
     "Rà soát lại locators để loại bỏ hoàn toàn flaky tests.",
     "Thống kê số lượng test cases và lập bảng đối chiếu kết quả kiểm thử.",
     "Bảng tổng hợp kết quả kiểm thử (Summary)", "Hoàn thành"),
    (41, "Tuần 7", "Thứ 6", "5. Test Suite & Đo lường",
     "Chạy nghiệm thu lại toàn bộ Test Suite trên môi trường sạch.",
     "Chuẩn hóa toàn bộ mã nguồn Java theo chuẩn Google Java Style.",
     "Đưa toàn bộ source code hoàn chỉnh vào file Word báo cáo.",
     "Toàn bộ source code đã tối ưu và định dạng", "Hoàn thành"),
    (42, "Tuần 7", "Thứ 7", "5. Test Suite & Đo lường",
     "Họp tổng kết giai đoạn lập trình, xác nhận hệ thống test chạy ổn định.",
     "Báo cáo tỷ lệ Pass Test Suite đạt yêu cầu.",
     "Ghi biên bản họp Tuần 7, chuẩn bị đóng gói nộp bài.",
     "Biên bản nghiệm thu hoàn thành mã nguồn", "Hoàn thành"),

    # TUAN 8
    (43, "Tuần 8", "Thứ 2", "6. Đóng gói & Nộp bài",
     "Hoàn thiện phần Mở đầu, Mục tiêu và Kế hoạch thực hiện đồ án trong file Word.",
     "Hoàn thiện phần Danh sách chức năng BCN Khoa kèm mô tả chi tiết.",
     "Căn chỉnh hình ảnh chụp màn hình UI, đánh số thứ tự Hình 1, Hình 2...",
     "File Word báo cáo hoàn thành Phần I & II", "Hoàn thành"),
    (44, "Tuần 8", "Thứ 3", "6. Đóng gói & Nộp bài",
     "Viết phần Giải thích kiến trúc kỹ thuật của Framework kiểm thử tự động.",
     "Hoàn thiện phần Giải thích chi tiết cho từng Test Script trong báo cáo.",
     "Soát lỗi chính tả, căn chỉnh lề (Margins) và kiểm tra định dạng Times New Roman 13pt.",
     "File Word báo cáo hoàn thành Phần III & IV", "Hoàn thành"),
    (45, "Tuần 8", "Thứ 4", "6. Đóng gói & Nộp bài",
     "Dọn dẹp thư mục dự án (xóa target/ rác) và đóng gói mã nguồn thành Team06_Ver1.0.zip.",
     "Giải nén file zip trên máy khác và chạy run_tests.bat để nghiệm thu độc lập.",
     "Xuất file báo cáo Word chính thức với tên Team06_Ver1.0.docx.",
     "Tệp Team06_Ver1.0.zip và Team06_Ver1.0.docx", "Hoàn thành"),
    (46, "Tuần 8", "Thứ 5", "6. Đóng gói & Nộp bài",
     "Tạo thư mục tổng 232_71ITSE41603_0102_Team06 chứa file Word và file Zip mã nguồn.",
     "Kiểm tra lại toàn bộ file theo Checklist quy định nộp bài của giảng viên.",
     "Nén thư mục tổng thành 232_71ITSE41603_0102_Team06.zip.",
     "Gói nộp bài hoàn chỉnh 232_71ITSE41603_0102_Team06.zip", "Hoàn thành"),
    (47, "Tuần 8", "Thứ 6", "6. Đóng gói & Nộp bài",
     "Nộp gói bài làm lên hệ thống E-learning của trường đúng thời hạn.",
     "Kiểm tra xác nhận bài nộp đã hiển thị thành công trên E-learning.",
     "Lưu trữ bản backup toàn bộ đồ án lên Google Drive của nhóm.",
     "Xác nhận nộp bài thành công trên E-learning", "Hoàn thành"),
    (48, "Tuần 8", "Thứ 7", "6. Đóng gói & Nộp bài",
     "Họp tổng kết đồ án, phân công chuẩn bị slide và nội dung báo cáo.",
     "Chuẩn bị phần trình bày về Test Cases và Automation Scripts.",
     "Chuẩn bị phần demo kết quả kiểm thử tự động trên hệ thống.",
     "Slide thuyết trình bảo vệ đồ án", "Sẵn sàng")
]

for row_idx, data in enumerate(daily_data, start=5):
    ws_schedule.row_dimensions[row_idx].height = 42
    is_zebra = (data[0] % 2 == 0)
    for col_idx, val in enumerate(data, start=1):
        c = ws_schedule.cell(row=row_idx, column=col_idx, value=val)
        c.font = font_data
        c.border = thin_border
        if is_zebra:
            c.fill = fill_zebra
        
        # Alignments
        if col_idx in [1, 2, 3]:
            c.alignment = Alignment(horizontal="center", vertical="center")
            c.font = font_data_bold
        elif col_idx in [4]:
            c.alignment = Alignment(horizontal="center", vertical="center")
        elif col_idx in [5, 6, 7]:
            c.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        elif col_idx in [8]:
            c.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
            c.font = font_data_bold
        elif col_idx in [9]:
            c.alignment = Alignment(horizontal="center", vertical="center")
            c.fill = fill_done
            c.font = font_done

col_w = {
    'A': 6,   # STT
    'B': 10,  # Tuần
    'C': 9,   # Thứ
    'D': 18,  # Giai đoạn
    'E': 38,  # Phú
    'F': 38,  # Khoa
    'G': 38,  # Thiệu
    'H': 32,  # Bàn giao
    'I': 14   # Trạng thái
}

for col_l, width in col_w.items():
    ws_schedule.column_dimensions[col_l].width = width

# ========================================================
# SHEET 3: TỔNG HỢP TIẾN ĐỘ & RACI MATRIX
# ========================================================
ws_summary.views.sheetView[0].showGridLines = True
ws_summary['A1'] = "TỔNG HỢP TIẾN ĐỘ THỰC HIỆN ĐỒ ÁN - TEAM 06"
ws_summary['A1'].font = font_title
ws_summary['A2'] = "Tóm tắt tiến độ 8 tuần & Ma trận phân công trách nhiệm (RACI Matrix)"
ws_summary['A2'].font = font_subtitle

summary_headers = [
    "Tuần", "Giai đoạn chính", "Mục tiêu trọng tâm", 
    "Nguyễn Minh Phú", "Trương Quốc Anh Khoa", "Bùi Ngọc Thiệu", 
    "Hạn chót (Deadline)", "Tiến độ"
]

for col_idx, h in enumerate(summary_headers, start=1):
    c = ws_summary.cell(row=4, column=col_idx, value=h)
    c.font = font_tbl_hdr
    c.fill = fill_hdr
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
ws_summary.row_dimensions[4].height = 28

weekly_summary = [
    ("Tuần 1", "Khởi động & Lập kế hoạch", "Nghiên cứu tài liệu, xác định mục tiêu và lập WBS", "Accountable (A)", "Responsible (R)", "Responsible (R)", "Thứ 7, Tuần 1", "100%"),
    ("Tuần 2", "Khảo sát hệ thống", "Khảo sát website, chụp UI và xác định các chức năng BCN Khoa", "Accountable (A)", "Responsible (R)", "Responsible (R)", "Thứ 7, Tuần 2", "100%"),
    ("Tuần 3", "Thiết kế Test Cases M1", "Thiết kế kịch bản kiểm thử Module Login & User Management", "Consulted (C)", "Responsible (R)", "Responsible (R)", "Thứ 7, Tuần 3", "100%"),
    ("Tuần 4", "Thiết kế Test Cases M2", "Thiết kế kịch bản kiểm thử Module Học kỳ, TKB, Thù lao", "Consulted (C)", "Responsible (R)", "Responsible (R)", "Thứ 7, Tuần 4", "100%"),
    ("Tuần 5", "Tự động hóa Module 1", "Dựng Base Framework POM, viết test script Login & User", "Responsible (R)", "Responsible (R)", "Support (S)", "Thứ 7, Tuần 5", "100%"),
    ("Tuần 6", "Tự động hóa Module 2", "Viết test script Module Học kỳ, Ngành, TKB (Import/Export)", "Support (S)", "Responsible (R)", "Responsible (R)", "Thứ 7, Tuần 6", "100%"),
    ("Tuần 7", "Test Suite & Đo lường", "Tích hợp testng.xml, chạy toàn bộ suite, fix lỗi, xuất report", "Accountable (A)", "Responsible (R)", "Responsible (R)", "Thứ 7, Tuần 7", "100%"),
    ("Tuần 8", "Đóng gói & Nộp bài", "Hoàn thiện Word Team06_Ver1.0.docx, nén zip và nộp E-learning", "Accountable (A)", "Responsible (R)", "Responsible (R)", "Thứ 6, Tuần 8", "100%")
]

for row_idx, s in enumerate(weekly_summary, start=5):
    ws_summary.row_dimensions[row_idx].height = 25
    for col_idx, val in enumerate(s, start=1):
        c = ws_summary.cell(row=row_idx, column=col_idx, value=val)
        c.font = font_data
        c.border = thin_border
        if col_idx in [1, 7]:
            c.alignment = Alignment(horizontal="center", vertical="center")
            c.font = font_data_bold
        elif col_idx in [2, 3]:
            c.alignment = Alignment(horizontal="left", vertical="center")
        elif col_idx in [4, 5, 6]:
            c.alignment = Alignment(horizontal="center", vertical="center")
        elif col_idx in [8]:
            c.alignment = Alignment(horizontal="center", vertical="center")
            c.fill = fill_done
            c.font = font_done

sum_col_w = {
    'A': 10,  # Tuần
    'B': 24,  # Giai đoạn
    'C': 42,  # Mục tiêu
    'D': 20,  # Phú
    'E': 22,  # Khoa
    'F': 20,  # Thiệu
    'G': 18,  # Hạn chót
    'H': 12   # Tiến độ
}

for col_l, width in sum_col_w.items():
    ws_summary.column_dimensions[col_l].width = width

# Save file
excel_path1 = r"D:\ktdt\Do an nhom\KeHoach_DoAnNhom_Team06.xlsx"
excel_path2 = r"D:\ktdt\Do an nhom\Team06_KeHoach.xlsx"

wb.save(excel_path1)
wb.save(excel_path2)
print("Successfully created KeHoach_DoAnNhom_Team06.xlsx and Team06_KeHoach.xlsx")
