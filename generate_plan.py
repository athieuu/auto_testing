import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

doc = docx.Document()

# Page margins
for section in doc.sections:
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)

# Header Title
p_school = doc.add_paragraph()
p_school.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_school = p_school.add_run('TRƯỜNG ĐẠI HỌC VĂN LANG\nKHOA CÔNG NGHỆ THÔNG TIN\n---***---')
run_school.bold = True
run_school.font.size = Pt(13)
run_school.font.name = 'Times New Roman'

p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_title = p_title.add_run('\nKẾ HOẠCH THỰC HIỆN ĐỒ ÁN NHÓM\n(LỊCH BIỂU CÔNG VIỆC CHI TIẾT THEO TUẦN VÀ THEO NGÀY)')
run_title.bold = True
run_title.font.size = Pt(15)
run_title.font.color.rgb = RGBColor(0, 51, 102)
run_title.font.name = 'Times New Roman'

p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_sub = p_sub.add_run('Môn học: Kiểm thử tự động (Khóa 27)\nĐề tài: Kiểm thử tự động ứng dụng Quản lý phân công giảng dạy (Vai trò: BCN Khoa)\n')
run_sub.font.size = Pt(12)
run_sub.font.italic = True
run_sub.font.name = 'Times New Roman'

# Team info
p_info = doc.add_paragraph()
r_info = p_info.add_run('1. THÔNG TIN CHUNG VỀ NHÓM THỰC HIỆN:\n')
r_info.bold = True
r_info.font.size = Pt(13)
r_info.font.color.rgb = RGBColor(0, 51, 102)

p_info_detail = doc.add_paragraph()
p_info_detail.paragraph_format.left_indent = Inches(0.2)
p_info_detail.add_run(
    '• Lớp học phần: 232_71ITSE41603_0102\n'
    '• Tên nhóm: Team 06\n'
    '• Danh sách thành viên nhóm (03 sinh viên):\n'
    '    1. Nguyễn Minh Phú - Nhóm trưởng (Quản lý tiến độ, xây dựng Base Framework, tự động hóa Module Login & User Management)\n'
    '    2. Trương Quốc Anh Khoa - Thành viên (Khảo sát hệ thống, thiết kế Test Cases chi tiết, tự động hóa Module Term & Major)\n'
    '    3. Bùi Ngọc Thiệu - Thành viên (Nghiên cứu quy định thù lao, tự động hóa Module Timetable & Thù lao, tổng hợp báo cáo và đóng gói nộp bài)\n'
    '• Ứng dụng kiểm thử: Quản lý phân công giảng dạy (https://cntttest.vanlanguni.edu.vn:18081/Phancong02/)\n'
    '• Phạm vi kiểm thử: Chức năng dành riêng cho vai trò BCN Khoa (Faculty Board)\n'
    '• Quy định tiến độ: Làm việc 6 ngày/tuần (từ Thứ 2 đến Thứ 7), chủ nhật nghỉ và tổng hợp tuần.\n'
)

# Section 2
p_s2 = doc.add_paragraph()
r_s2 = p_s2.add_run('2. BẢNG LỊCH BIỂU CÔNG VIỆC CHI TIẾT TỪNG NGÀY TRONG TUẦN (WBS & DAILY TIMELINE):\n')
r_s2.bold = True
r_s2.font.size = Pt(13)
r_s2.font.color.rgb = RGBColor(0, 51, 102)

headers = ['Tuần', 'Thứ', 'Nhiệm vụ cụ thể của từng thành viên', 'Sản phẩm bàn giao', 'Trạng thái']

daily_tasks = [
    # TUAN 1
    ('Tuần 1', 'Thứ 2', 
     '• Nguyễn Minh Phú (NT): Họp nhóm kick-off, quán triệt đề bài FinalAssignment 1, tạo nhóm Zalo và Google Drive.\n'
     '• Trương Quốc Anh Khoa: Tải và đọc tài liệu ProductBacklog.xlsx, FunctionList_V1.8.xlsx.\n'
     '• Bùi Ngọc Thiệu: Tải và đọc tài liệu UserGuide.pdf, Quy định tính thù lao.docx.',
     'Biên bản họp nhóm kick-off, Thư mục lưu trữ chung', 'Hoàn thành'),
    ('Tuần 1', 'Thứ 3',
     '• Nguyễn Minh Phú: Phân tích cấu trúc thư mục nộp bài (LopTH_Team#) và quy định báo cáo hàng tuần.\n'
     '• Trương Quốc Anh Khoa: Lọc toàn bộ các chức năng thuộc vai trò BCN Khoa từ FunctionList.\n'
     '• Bùi Ngọc Thiệu: Đọc hiểu các thuật ngữ chuyên môn trong phần mềm Quản lý phân công giảng dạy.',
     'Bản tóm tắt quy định đề bài & Danh mục thuật ngữ', 'Hoàn thành'),
    ('Tuần 1', 'Thứ 4',
     '• Nguyễn Minh Phú: Phác thảo khung lịch biểu 8 tuần làm việc (6 ngày/tuần).\n'
     '• Trương Quốc Anh Khoa: Xác định các mốc bàn giao Test Cases và Automation Scripts.\n'
     '• Bùi Ngọc Thiệu: Đóng góp ý kiến về thời lượng từng module kiểm thử.',
     'Khung lịch biểu làm việc nhóm sơ bộ', 'Hoàn thành'),
    ('Tuần 1', 'Thứ 5',
     '• Nguyễn Minh Phú: Dự thảo file Word kế hoạch thực hiện đồ án nhóm.\n'
     '• Trương Quốc Anh Khoa: Rà soát tính khả thi và phân công trách nhiệm từng thành viên.\n'
     '• Bùi Ngọc Thiệu: Chuẩn bị biểu mẫu nhật ký công việc (Work log).',
     'Dự thảo bản kế hoạch công việc (.docx)', 'Hoàn thành'),
    ('Tuần 1', 'Thứ 6',
     '• Nguyễn Minh Phú: Hoàn thiện bảng kế hoạch đồ án nhóm chi tiết theo ngày.\n'
     '• Trương Quốc Anh Khoa: Kiểm tra chéo phân công nhiệm vụ, đối chiếu yêu cầu đề bài.\n'
     '• Bùi Ngọc Thiệu: Thiết lập kho mã nguồn chung trên Git/GitHub và Drive.',
     'File kế hoạch hoàn chỉnh, Repo Git của nhóm', 'Hoàn thành'),
    ('Tuần 1', 'Thứ 7',
     '• Cả nhóm (Phú, Khoa, Thiệu): Họp online tổng kết Tuần 1, nghiệm thu kế hoạch công việc và phân công chi tiết Tuần 2.',
     'Biên bản nghiệm thu Tuần 1', 'Hoàn thành'),

    # TUAN 2
    ('Tuần 2', 'Thứ 2',
     '• Nguyễn Minh Phú: Truy cập hệ thống https://cntttest.vanlanguni.edu.vn:18081/Phancong02/, kiểm tra quyền BCN Khoa.\n'
     '• Trương Quốc Anh Khoa: Thử nghiệm luồng giao diện người dùng vai trò BCN Khoa.\n'
     '• Bùi Ngọc Thiệu: Chụp màn hình trang chủ và thanh menu điều hướng BCN Khoa.',
     'Hình ảnh giao diện trang chủ BCN Khoa', 'Hoàn thành'),
    ('Tuần 2', 'Thứ 3',
     '• Nguyễn Minh Phú: Khảo sát chi tiết Module Quản lý Người dùng (User Management).\n'
     '• Trương Quốc Anh Khoa: Khảo sát chi tiết Module Quản lý Học kỳ (Term) và Ngành (Major).\n'
     '• Bùi Ngọc Thiệu: Khảo sát chi tiết Module Thời khóa biểu (Import, Export, Phân công).',
     'Ghi chú luồng hoạt động từng Module', 'Hoàn thành'),
    ('Tuần 2', 'Thứ 4',
     '• Nguyễn Minh Phú: Lập danh sách các phần tử HTML (ID, Name, XPath) của Module User.\n'
     '• Trương Quốc Anh Khoa: Liệt kê các trường dữ liệu bắt buộc của Module Term và Major.\n'
     '• Bùi Ngọc Thiệu: Khảo sát giao diện Thống kê và Bảng tính thù lao giảng dạy.',
     'Bảng danh mục Element Locators sơ bộ', 'Hoàn thành'),
    ('Tuần 2', 'Thứ 5',
     '• Nguyễn Minh Phú: Phân loại các chức năng có thể tự động hóa (Automated) vs thủ công.\n'
     '• Trương Quốc Anh Khoa: Tổng hợp danh sách chức năng BCN Khoa đưa vào báo cáo Word.\n'
     '• Bùi Ngọc Thiệu: Chụp toàn bộ ảnh giao diện từng chức năng BCN Khoa.',
     'Bộ ảnh chụp màn hình UI đầy đủ của BCN Khoa', 'Hoàn thành'),
    ('Tuần 2', 'Thứ 6',
     '• Nguyễn Minh Phú: Soạn thảo nội dung phần 1 của file báo cáo Word (Danh sách chức năng BCN Khoa).\n'
     '• Trương Quốc Anh Khoa: Đối chiếu danh sách chức năng với Product Backlog để đảm bảo không sót.\n'
     '• Bùi Ngọc Thiệu: Chèn và căn chỉnh hình ảnh chụp màn hình vào file Word.',
     'Bản thảo báo cáo phần Danh sách chức năng BCN Khoa', 'Hoàn thành'),
    ('Tuần 2', 'Thứ 7',
     '• Cả nhóm: Họp online nghiệm thu kết quả khảo sát Tuần 2, chuẩn bị chuyển sang thiết kế Test Cases.',
     'Biên bản họp nghiệm thu Tuần 2', 'Hoàn thành'),

    # TUAN 3
    ('Tuần 3', 'Thứ 2',
     '• Nguyễn Minh Phú: Thống nhất cấu trúc template Test Case Excel (ID, Description, Pre-condition, Steps, Expected).\n'
     '• Trương Quốc Anh Khoa: Viết kịch bản kiểm thử chức năng Đăng nhập F.1.1 (hợp lệ, sai pass, bỏ trống).\n'
     '• Bùi Ngọc Thiệu: Chuẩn bị danh sách tài khoản kiểm thử (Test Accounts BCN Khoa).',
     'File Test Cases Module Đăng nhập (Excel)', 'Hoàn thành'),
    ('Tuần 3', 'Thứ 3',
     '• Nguyễn Minh Phú: Hướng dẫn kỹ thuật phân vùng tương đương và giá trị biên cho form Thêm người dùng.\n'
     '• Trương Quốc Anh Khoa: Thiết kế Test Cases cho F.2.1 (Xem DS) và F.2.2 (Thêm mới người dùng).\n'
     '• Bùi Ngọc Thiệu: Chuẩn bị dữ liệu kiểm thử người dùng (Mã GV, Tên, Email VLU).',
     'Test Cases Thêm mới người dùng', 'Hoàn thành'),
    ('Tuần 3', 'Thứ 4',
     '• Nguyễn Minh Phú: Review Test Cases Thêm mới người dùng, bổ sung case trùng mã GV/email.\n'
     '• Trương Quốc Anh Khoa: Thiết kế Test Cases cho F.2.3 (Cập nhật) và F.2.4 (Xóa người dùng).\n'
     '• Bùi Ngọc Thiệu: Thiết kế Test Cases cho F.2.5 (Tìm kiếm) và F.2.6 (Khóa tài khoản).',
     'Test Cases Cập nhật, Xóa, Tìm kiếm, Khóa user', 'Hoàn thành'),
    ('Tuần 3', 'Thứ 5',
     '• Nguyễn Minh Phú: Thiết kế các Test Cases kiểm thử biên cho trường Mã GV và định dạng Email.\n'
     '• Trương Quốc Anh Khoa: Bổ sung các kịch bản kiểm tra thông báo lỗi validation trên giao diện.\n'
     '• Bùi Ngọc Thiệu: Tổng hợp bảng Test Data hoàn chỉnh vào Excel.',
     'Bộ dữ liệu Test Data chuẩn cho Module 1', 'Hoàn thành'),
    ('Tuần 3', 'Thứ 6',
     '• Nguyễn Minh Phú: Rà soát toàn diện bộ Test Cases Module Login & User Management.\n'
     '• Trương Quốc Anh Khoa: Chuẩn hóa mã định danh Test Case (TC_LOGIN_xx, TC_USER_xx).\n'
     '• Bùi Ngọc Thiệu: Cập nhật nội dung bảng Test Cases vào file Word báo cáo.',
     'Tài liệu Test Cases Module 1 hoàn chỉnh', 'Hoàn thành'),
    ('Tuần 3', 'Thứ 7',
     '• Cả nhóm: Họp nghiệm thu bộ Test Cases Module 1, đánh giá độ bao phủ đạt yêu cầu.',
     'Biên bản nghiệm thu Tuần 3', 'Hoàn thành'),

    # TUAN 4
    ('Tuần 4', 'Thứ 2',
     '• Nguyễn Minh Phú: Phân tích quy tắc nghiệp vụ Module Quản lý Học kỳ (F.3).\n'
     '• Trương Quốc Anh Khoa: Viết Test Cases cho F.3.1 (Xem DS), F.3.2 (Tạo mới), F.3.3 (Cập nhật HK).\n'
     '• Bùi Ngọc Thiệu: Viết Test Cases cho F.3.4 (Xóa HK), F.3.5 (Tìm kiếm), F.3.6 (Khóa học kỳ).',
     'Test Cases Module Quản lý Học kỳ', 'Hoàn thành'),
    ('Tuần 4', 'Thứ 3',
     '• Nguyễn Minh Phú: Thiết kế Test Cases cho Module Quản lý Ngành (F.4.1 - F.4.5).\n'
     '• Trương Quốc Anh Khoa: Chuẩn bị dữ liệu kiểm thử ngành học (Mã ngành, tên ngành).\n'
     '• Bùi Ngọc Thiệu: Nghiên cứu cấu trúc tệp Excel thời khóa biểu chuẩn dùng để Import.',
     'Test Cases Module Quản lý Ngành', 'Hoàn thành'),
    ('Tuần 4', 'Thứ 4',
     '• Nguyễn Minh Phú: Thiết kế Test Cases cho F.5.1 (Import TKB: file hợp lệ, sai định dạng, file trống).\n'
     '• Trương Quốc Anh Khoa: Thiết kế Test Cases cho F.5.2 (Export TKB) và F.5.3 (Xem TKB toàn khoa).\n'
     '• Bùi Ngọc Thiệu: Thiết kế Test Cases cho F.5.4 (Phân công giảng viên) và F.5.5 (Xóa lớp HP).',
     'Test Cases Import/Export và Phân công TKB', 'Hoàn thành'),
    ('Tuần 4', 'Thứ 5',
     '• Nguyễn Minh Phú: Thiết kế Test Cases cho Module Thống kê (F.6) và Thù lao (F.7).\n'
     '• Trương Quốc Anh Khoa: Bổ sung kịch bản kiểm tra logic tính giờ theo công thức quy định.\n'
     '• Bùi Ngọc Thiệu: Tạo tệp Excel TKB thử nghiệm mẫu chứa các lớp học phần phục vụ test.',
     'Tệp Excel TKB test mẫu', 'Hoàn thành'),
    ('Tuần 4', 'Thứ 6',
     '• Nguyễn Minh Phú: Rà soát ma trận truy xuất nguồn gốc (Traceability Matrix) giữa yêu cầu và Test Cases.\n'
     '• Trương Quốc Anh Khoa: Đồng bộ hóa toàn bộ mã định danh Test Case (TC_TERM_xx, TC_TKB_xx).\n'
     '• Bùi Ngọc Thiệu: Tổng hợp toàn bộ Test Cases giai đoạn 2 vào file Word báo cáo.',
     'Tài liệu đặc tả Test Cases toàn hệ thống', 'Hoàn thành'),
    ('Tuần 4', 'Thứ 7',
     '• Cả nhóm: Họp tổng kết giai đoạn Thiết kế Test Cases, thống nhất phương án viết mã nguồn tự động hóa.',
     'Biên bản chốt danh sách Test Case tự động hóa', 'Hoàn thành'),

    # TUAN 5
    ('Tuần 5', 'Thứ 2',
     '• Nguyễn Minh Phú: Khởi tạo Maven Project, cấu hình pom.xml (Selenium 4.25, TestNG 7.10, Surefire).\n'
     '• Trương Quốc Anh Khoa: Viết lớp BasePage.java xử lý Explicit Wait, Click, SendKeys.\n'
     '• Bùi Ngọc Thiệu: Viết lớp BaseTest.java quản lý vòng đời ChromeDriver, Timeouts, Window Maximize.',
     'Base Framework POM hoàn chỉnh', 'Hoàn thành'),
    ('Tuần 5', 'Thứ 3',
     '• Nguyễn Minh Phú: Xây dựng LoginPage.java (locators và phương thức login, logout).\n'
     '• Trương Quốc Anh Khoa: Viết test class LoginTest.java với các test case đăng nhập hợp lệ/không hợp lệ.\n'
     '• Bùi Ngọc Thiệu: Chạy thử nghiệm LoginTest, kiểm tra tính ổn định trên Chrome.',
     'Mã nguồn LoginPage.java và LoginTest.java', 'Hoàn thành'),
    ('Tuần 5', 'Thứ 4',
     '• Nguyễn Minh Phú: Xây dựng UserManagementPage.java (các locator bảng người dùng, form thêm/sửa/xóa).\n'
     '• Trương Quốc Anh Khoa: Viết test method kiểm tra Xem danh sách và Tìm kiếm người dùng.\n'
     '• Bùi Ngọc Thiệu: Viết test method Thêm mới người dùng với assertion thông báo thành công.',
     'Mã nguồn UserManagementPage.java', 'Hoàn thành'),
    ('Tuần 5', 'Thứ 5',
     '• Nguyễn Minh Phú: Viết kịch bản tự động Cập nhật thông tin và Xóa người dùng.\n'
     '• Trương Quốc Anh Khoa: Áp dụng @DataProvider kiểm thử form User với nhiều tập dữ liệu.\n'
     '• Bùi Ngọc Thiệu: Viết kịch bản tự động kiểm thử chức năng Khóa tài khoản giảng viên.',
     'Mã nguồn UserManagementTest.java', 'Hoàn thành'),
    ('Tuần 5', 'Thứ 6',
     '• Nguyễn Minh Phú: Tối ưu mã nguồn Module 1, push code lên Git repo chung.\n'
     '• Trương Quốc Anh Khoa: Đo thời gian chạy của test case và điều chỉnh wait hợp lý.\n'
     '• Bùi Ngọc Thiệu: Viết tài liệu giải thích source code Module Login & User vào file báo cáo Word.',
     'Báo cáo giải thích source code Module 1', 'Hoàn thành'),
    ('Tuần 5', 'Thứ 7',
     '• Cả nhóm: Họp review mã nguồn Module 1, chạy kiểm thử xác nhận tất cả test case Pass.',
     'Biên bản nghiệm thu mã nguồn Tuần 5', 'Hoàn thành'),

    # TUAN 6
    ('Tuần 6', 'Thứ 2',
     '• Nguyễn Minh Phú: Thiết kế kiến trúc Page Object cho Module Quản lý Học kỳ và Ngành.\n'
     '• Trương Quốc Anh Khoa: Xây dựng TermManagementPage.java và TermManagementTest.java.\n'
     '• Bùi Ngọc Thiệu: Xây dựng MajorManagementPage.java và MajorManagementTest.java.',
     'Page Objects cho Học kỳ và Ngành', 'Hoàn thành'),
    ('Tuần 6', 'Thứ 3',
     '• Nguyễn Minh Phú: Kiểm tra tính độc lập và xử lý dữ liệu động cho TermManagementTest.\n'
     '• Trương Quốc Anh Khoa: Hoàn thiện kịch bản Tạo học kỳ mới (F.3.2) và Khóa học kỳ (F.3.6).\n'
     '• Bùi Ngọc Thiệu: Hoàn thiện kịch bản Thêm, Sửa, Xóa ngành học (F.4.1 - F.4.4).',
     'Mã nguồn TermManagementTest.java', 'Hoàn thành'),
    ('Tuần 6', 'Thứ 4',
     '• Nguyễn Minh Phú: Xây dựng TimetableManagementPage.java xử lý upload tệp và thao tác bảng TKB.\n'
     '• Trương Quốc Anh Khoa: Viết kịch bản tự động kiểm thử chức năng Import TKB từ tệp Excel (F.5.1).\n'
     '• Bùi Ngọc Thiệu: Viết kịch bản tự động kiểm thử chức năng Export TKB (F.5.2) và Xem TKB (F.5.3).',
     'Mã nguồn TimetableManagementPage.java', 'Hoàn thành'),
    ('Tuần 6', 'Thứ 5',
     '• Nguyễn Minh Phú: Viết kịch bản tự động Phân công giảng viên vào lớp học phần (F.5.4).\n'
     '• Trương Quốc Anh Khoa: Viết kịch bản tự động Xóa lớp học phần trên thời khóa biểu (F.5.5).\n'
     '• Bùi Ngọc Thiệu: Viết kịch bản kiểm thử Xem thời khóa biểu cá nhân của BCN Khoa (F.5.6).',
     'Mã nguồn TimetableManagementTest.java', 'Hoàn thành'),
    ('Tuần 6', 'Thứ 6',
     '• Nguyễn Minh Phú: Bổ sung xử lý ngoại lệ (Exception Handling) khi mạng lag hoặc trang load chậm.\n'
     '• Trương Quốc Anh Khoa: Chạy kiểm thử tự động toàn bộ Module 2 trên Chrome browser.\n'
     '• Bùi Ngọc Thiệu: Cập nhật source code và giải thích chi tiết Module 2 vào file Word báo cáo.',
     'Báo cáo giải thích source code Module 2', 'Hoàn thành'),
    ('Tuần 6', 'Thứ 7',
     '• Cả nhóm: Họp nghiệm thu mã nguồn Module 2, tổng hợp log và chuẩn bị cho việc tích hợp Suite.',
     'Biên bản nghiệm thu Tuần 6', 'Hoàn thành'),

    # TUAN 7
    ('Tuần 7', 'Thứ 2',
     '• Nguyễn Minh Phú: Xây dựng StatisticsPage.java và RemunerationPage.java.\n'
     '• Trương Quốc Anh Khoa: Viết kịch bản kiểm thử Thống kê giờ dạy theo học kỳ và năm (F.6.1 - F.6.2).\n'
     '• Bùi Ngọc Thiệu: Viết kịch bản kiểm thử Bảng tính thù lao giảng dạy (F.7.19).',
     'Mã nguồn StatisticsPage & RemunerationPage', 'Hoàn thành'),
    ('Tuần 7', 'Thứ 3',
     '• Nguyễn Minh Phú: Tạo file testng.xml cấu hình toàn bộ Suite kiểm thử của vai trò BCN Khoa.\n'
     '• Trương Quốc Anh Khoa: Thiết lập độ ưu tiên (priority) và phụ thuộc giữa các test class.\n'
     '• Bùi Ngọc Thiệu: Viết file run_tests.bat hỗ trợ chạy kiểm thử 1-click không cần IDE.',
     'File testng.xml và run_tests.bat', 'Hoàn thành'),
    ('Tuần 7', 'Thứ 4',
     '• Nguyễn Minh Phú: Thực thi toàn bộ Test Suite bằng lệnh Maven Surefire test.\n'
     '• Trương Quốc Anh Khoa: Ghi nhận kết quả thực thi (Pass rate, Fail rate, lỗi phát sinh).\n'
     '• Bùi Ngọc Thiệu: Chụp ảnh kết quả TestNG Report và Console output.',
     'Surefire Report & TestNG HTML Report', 'Hoàn thành'),
    ('Tuần 7', 'Thứ 5',
     '• Nguyễn Minh Phú: Phân tích các trường hợp fail, sửa lỗi assertion và tối ưu timeout.\n'
     '• Trương Quốc Anh Khoa: Rà soát lại locators để loại bỏ hoàn toàn flaky tests.\n'
     '• Bùi Ngọc Thiệu: Thống kê số lượng test cases và lập bảng đối chiếu kết quả kiểm thử.',
     'Bảng tổng hợp kết quả kiểm thử (Summary)', 'Hoàn thành'),
    ('Tuần 7', 'Thứ 6',
     '• Nguyễn Minh Phú: Chạy nghiệm thu lại toàn bộ Test Suite trên môi trường sạch.\n'
     '• Trương Quốc Anh Khoa: Chuẩn hóa toàn bộ mã nguồn Java theo chuẩn Google Java Style.\n'
     '• Bùi Ngọc Thiệu: Đưa toàn bộ source code hoàn chỉnh vào file Word báo cáo.',
     'Toàn bộ source code đã tối ưu và định dạng', 'Hoàn thành'),
    ('Tuần 7', 'Thứ 7',
     '• Cả nhóm: Họp tổng kết giai đoạn lập trình, xác nhận hệ thống test chạy ổn định, chuẩn bị nộp bài.',
     'Biên bản nghiệm thu hoàn thành mã nguồn', 'Hoàn thành'),

    # TUAN 8
    ('Tuần 8', 'Thứ 2',
     '• Nguyễn Minh Phú: Hoàn thiện phần Mở đầu, Mục tiêu và Kế hoạch thực hiện đồ án trong file Word.\n'
     '• Trương Quốc Anh Khoa: Hoàn thiện phần Danh sách chức năng BCN Khoa kèm mô tả chi tiết.\n'
     '• Bùi Ngọc Thiệu: Căn chỉnh hình ảnh chụp màn hình UI, đánh số thứ tự Hình 1, Hình 2...',
     'File Word báo cáo hoàn thành Phần I & II', 'Hoàn thành'),
    ('Tuần 8', 'Thứ 3',
     '• Nguyễn Minh Phú: Viết phần Giải thích kiến trúc kỹ thuật của Framework kiểm thử tự động.\n'
     '• Trương Quốc Anh Khoa: Hoàn thiện phần Giải thích chi tiết cho từng Test Script trong báo cáo.\n'
     '• Bùi Ngọc Thiệu: Soát lỗi chính tả, căn chỉnh lề (Margins) và kiểm tra định dạng Times New Roman 13pt.',
     'File Word báo cáo hoàn thành Phần III & IV', 'Hoàn thành'),
    ('Tuần 8', 'Thứ 4',
     '• Nguyễn Minh Phú: Dọn dẹp thư mục dự án (xóa target/ rác) và đóng gói mã nguồn thành Team06_Ver1.0.zip.\n'
     '• Trương Quốc Anh Khoa: Giải nén file zip trên máy khác và chạy run_tests.bat để nghiệm thu độc lập.\n'
     '• Bùi Ngọc Thiệu: Xuất file báo cáo Word chính thức với tên Team06_Ver1.0.docx.',
     'Tệp Team06_Ver1.0.zip và Team06_Ver1.0.docx', 'Hoàn thành'),
    ('Tuần 8', 'Thứ 5',
     '• Nguyễn Minh Phú: Tạo thư mục tổng 232_71ITSE41603_0102_Team06 chứa file Word và file Zip mã nguồn.\n'
     '• Trương Quốc Anh Khoa: Kiểm tra lại toàn bộ file theo Checklist quy định nộp bài của giảng viên.\n'
     '• Bùi Ngọc Thiệu: Nén thư mục tổng thành 232_71ITSE41603_0102_Team06.zip.',
     'Gói nộp bài hoàn chỉnh 232_71ITSE41603_0102_Team06.zip', 'Hoàn thành'),
    ('Tuần 8', 'Thứ 6',
     '• Nguyễn Minh Phú (NT): Nộp gói bài làm lên hệ thống E-learning của trường đúng thời hạn.\n'
     '• Trương Quốc Anh Khoa: Kiểm tra xác nhận bài nộp đã hiển thị thành công trên E-learning.\n'
     '• Bùi Ngọc Thiệu: Lưu trữ bản backup toàn bộ đồ án lên Google Drive của nhóm.',
     'Xác nhận nộp bài thành công trên E-learning', 'Hoàn thành'),
    ('Tuần 8', 'Thứ 7',
     '• Cả nhóm (Phú, Khoa, Thiệu): Họp tổng kết đồ án, phân công chuẩn bị slide và nội dung báo cáo trước giảng viên.',
     'Slide thuyết trình bảo vệ đồ án', 'Sẵn sàng')
]

table = doc.add_table(rows=1, cols=len(headers))
table.alignment = WD_TABLE_ALIGNMENT.CENTER
table.autofit = False

hdr_cells = table.rows[0].cells
for i, h in enumerate(headers):
    hdr_cells[i].text = h
    shading_xml = parse_xml(r'<w:shd {} w:fill="003366"/>'.format(nsdecls('w')))
    hdr_cells[i]._tc.get_or_add_tcPr().append(shading_xml)
    for p in hdr_cells[i].paragraphs:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)
            r.font.size = Pt(10)
            r.font.name = 'Times New Roman'

col_widths = [Inches(0.7), Inches(0.6), Inches(4.3), Inches(1.3), Inches(0.8)]

for task in daily_tasks:
    row_cells = table.add_row().cells
    for i, val in enumerate(task):
        row_cells[i].text = val
        for p in row_cells[i].paragraphs:
            if i in [0, 1, 4]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.size = Pt(9.5)
                r.font.name = 'Times New Roman'

for row in table.rows:
    for i, w in enumerate(col_widths):
        row.cells[i].width = w

# Section 3
p_s3 = doc.add_paragraph()
r_s3 = p_s3.add_run('\n3. QUY CHẾ LÀM VIỆC NHÓM VÀ BÁO CÁO TIẾN ĐỘ:\n')
r_s3.bold = True
r_s3.font.size = Pt(13)
r_s3.font.color.rgb = RGBColor(0, 51, 102)

p_rule = doc.add_paragraph()
p_rule.paragraph_format.left_indent = Inches(0.2)
p_rule.add_run(
    '• Chế độ làm việc: Mỗi tuần làm việc 6 ngày (từ Thứ 2 đến Thứ 7), chủ nhật nghỉ ngơi và tổng hợp tuần.\n'
    '• Chế độ họp nhóm: Họp định kỳ 1 lần/tuần vào tối thứ 7 qua Google Meet để nghiệm thu công việc trong tuần và giao việc tuần kế tiếp.\n'
    '• Kênh trao đổi chính: Nhóm Zalo trao đổi hằng ngày và Google Drive / Git để chia sẻ tài liệu và mã nguồn.\n'
    '• Trách nhiệm thành viên: Mỗi thành viên tự chịu trách nhiệm về phần việc được giao, báo cáo tiến độ hằng ngày cho Nhóm trưởng Nguyễn Minh Phú.\n'
    '• Quy chuẩn bài nộp: Cập nhật file Word tăng dần theo phiên bản (Team06_Ver1.0, Ver1.1...) đúng theo quy định trong đề bài.\n'
)

# Signature
p_sign = doc.add_paragraph()
p_sign.alignment = WD_ALIGN_PARAGRAPH.RIGHT
p_sign.add_run('\nTP. Hồ Chí Minh, ngày .... tháng .... năm 2026\nĐẠI DIỆN NHÓM (TRƯỞNG NHÓM)\n\n\n\nNguyễn Minh Phú')

doc.save(r'D:\ktdt\Do an nhom\KeHoach_DoAnNhom_Team06.docx')
doc.save(r'D:\ktdt\Do an nhom\Team06_Ver1.0.docx')
print('Successfully generated KeHoach_DoAnNhom_Team06.docx and Team06_Ver1.0.docx with daily breakdown')
