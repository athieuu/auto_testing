import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
import os

doc = docx.Document()

# Set standard A4 margins (0.75 inch)
for section in doc.sections:
    section.top_margin = Inches(0.75)
    section.bottom_margin = Inches(0.75)
    section.left_margin = Inches(0.75)
    section.right_margin = Inches(0.75)

# Color constants
COLOR_NAVY = RGBColor(0, 51, 102)
COLOR_GRAY = RGBColor(80, 80, 80)

def add_heading_1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run(text)
    r.bold = True
    r.font.name = "Times New Roman"
    r.font.size = Pt(14)
    r.font.color.rgb = COLOR_NAVY
    return p

def add_heading_2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(text)
    r.bold = True
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)
    r.font.color.rgb = RGBColor(31, 73, 125)
    return p

def add_body(text, bold=False, italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    r = p.add_run(text)
    r.bold = bold
    r.font.italic = italic
    r.font.name = "Times New Roman"
    r.font.size = Pt(11)
    return p

def format_cell(cell, text, bold=False, align=WD_ALIGN_PARAGRAPH.LEFT, font_size=9.5, fill_hex=None, text_color="000000"):
    cell.text = text
    if fill_hex:
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
        cell._tc.get_or_add_tcPr().append(shd)
    for p in cell.paragraphs:
        p.alignment = align
        for r in p.runs:
            r.bold = bold
            r.font.size = Pt(font_size)
            r.font.name = "Times New Roman"
            if text_color != "000000":
                r.font.color.rgb = RGBColor(int(text_color[:2], 16), int(text_color[2:4], 16), int(text_color[4:], 16))

# -------------------------------------------------------------
# COVER PAGE / TIÊU ĐỀ
# -------------------------------------------------------------
p_hdr = doc.add_paragraph()
p_hdr.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_hdr1 = p_hdr.add_run("TRƯỜNG ĐẠI HỌC VĂN LANG\nKHOA CÔNG NGHỆ THÔNG TIN\n")
r_hdr1.bold = True
r_hdr1.font.size = Pt(13)
r_hdr1.font.name = "Times New Roman"
r_hdr2 = p_hdr.add_run("---***---\n\n\n")

p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_title = p_title.add_run("BÁO CÁO TIẾN ĐỘ ĐỒ ÁN NHÓM (TUẦN 2)\n")
r_title.bold = True
r_title.font.size = Pt(18)
r_title.font.color.rgb = COLOR_NAVY
r_title.font.name = "Times New Roman"

r_title_sub = p_title.add_run("MÔN HỌC: KIỂM THỬ TỰ ĐỘNG (KHÓA 27)\n")
r_title_sub.bold = True
r_title_sub.font.size = Pt(13)
r_title_sub.font.name = "Times New Roman"

r_sub = p_title.add_run("Đề tài: Kiểm thử tự động ứng dụng Quản lý phân công giảng dạy\nPhạm vi: Các chức năng thuộc vai trò BCN Khoa (Faculty Board)\n\n")
r_sub.font.size = Pt(12)
r_sub.font.italic = True
r_sub.font.name = "Times New Roman"

# Student Table on Cover
tbl_info = doc.add_table(rows=6, cols=2)
tbl_info.alignment = WD_TABLE_ALIGNMENT.CENTER
info_data = [
    ("Lớp học phần:", "232_71ITSE41603_0102"),
    ("Nhóm thực hiện:", "Team 06"),
    ("Thành viên 1 (Nhóm trưởng):", "Nguyễn Minh Phú"),
    ("Thành viên 2:", "Trương Quốc Anh Khoa"),
    ("Thành viên 3:", "Bùi Ngọc Thiệu"),
    ("Thời gian báo cáo:", "Tuần 2 - Tháng 10/2026")
]
for idx, (label, val) in enumerate(info_data):
    format_cell(tbl_info.rows[idx].cells[0], label, bold=True, font_size=11)
    format_cell(tbl_info.rows[idx].cells[1], val, font_size=11)
    tbl_info.rows[idx].cells[0].width = Inches(2.5)
    tbl_info.rows[idx].cells[1].width = Inches(4.0)

doc.add_page_break()

# -------------------------------------------------------------
# PHẦN 1: KẾ HOẠCH VÀ TIẾN ĐỘ THỰC HIỆN ĐẾN TUẦN 2
# -------------------------------------------------------------
add_heading_1("PHẦN 1: KẾ HOẠCH THỰC HIỆN ĐỒ ÁN VÀ TIẾN ĐỘ TUẦN 1 - TUẦN 2")

add_heading_2("1.1. Mục tiêu và Kế hoạch tổng thể (8 tuần)")
add_body(
    "Theo yêu cầu của đề tài FinalAssignment 1, nhóm đã lập kế hoạch phân rã công việc (Work Breakdown Structure - WBS) "
    "trong thời gian 8 tuần, làm việc với cường độ 6 ngày/tuần (từ Thứ 2 đến Thứ 7). "
    "Bản kế hoạch tập trung lên lịch biểu chi tiết cho từng thành viên, đảm bảo tuân thủ đúng yêu cầu chỉ kiểm thử các chức năng của vai trò BCN Khoa."
)

add_heading_2("1.2. Nhật ký tiến độ thực hiện chi tiết Tuần 1 và Tuần 2")
add_body(
    "Dưới đây là bảng tổng hợp công việc thực tế mà 3 thành viên (Nguyễn Minh Phú, Trương Quốc Anh Khoa, Bùi Ngọc Thiệu) "
    "đã hoàn thành trong Tuần 1 và Tuần 2:"
)

# Daily Progress Table for Weeks 1 and 2
sched_headers = ["Tuần", "Thứ", "Nhiệm vụ cụ thể của từng thành viên", "Sản phẩm bàn giao", "Trạng thái"]
progress_rows = [
    # Tuần 1
    ("Tuần 1", "Thứ 2", 
     "• Nguyễn Minh Phú (NT): Họp nhóm kick-off, quán triệt đề bài FinalAssignment 1, tạo nhóm Zalo và Drive chung.\n"
     "• Trương Quốc Anh Khoa: Tải và đọc ProductBacklog.xlsx, FunctionList_V1.8.xlsx.\n"
     "• Bùi Ngọc Thiệu: Tải và đọc UserGuide.pdf, Quy định tính thù lao.docx.", 
     "Biên bản họp kick-off, Thư mục tài liệu chung", "Hoàn thành"),
    ("Tuần 1", "Thứ 3",
     "• Nguyễn Minh Phú: Phân tích cấu trúc thư mục nộp bài (LopTH_Team#) và quy chế nộp bài hằng tuần.\n"
     "• Trương Quốc Anh Khoa: Lọc toàn bộ các chức năng của BCN Khoa từ FunctionList.\n"
     "• Bùi Ngọc Thiệu: Đọc hiểu các thuật ngữ chuyên môn trong phần mềm Quản lý phân công.",
     "Bản tóm tắt quy định đề bài & Danh mục thuật ngữ", "Hoàn thành"),
    ("Tuần 1", "Thứ 4",
     "• Nguyễn Minh Phú: Phác thảo khung lịch biểu 8 tuần (6 ngày/tuần).\n"
     "• Trương Quốc Anh Khoa: Xác định mốc bàn giao Test Cases và Automation Scripts.\n"
     "• Bùi Ngọc Thiệu: Đóng góp ý kiến về phân bổ thời lượng các module.",
     "Khung lịch biểu làm việc nhóm sơ bộ", "Hoàn thành"),
    ("Tuần 1", "Thứ 5",
     "• Nguyễn Minh Phú: Dự thảo file Word kế hoạch thực hiện đồ án nhóm.\n"
     "• Trương Quốc Anh Khoa: Rà soát tính khả thi và phân công trách nhiệm 3 thành viên.\n"
     "• Bùi Ngọc Thiệu: Chuẩn bị biểu mẫu nhật ký công việc (Work log).",
     "Dự thảo bản kế hoạch công việc (.docx)", "Hoàn thành"),
    ("Tuần 1", "Thứ 6",
     "• Nguyễn Minh Phú: Hoàn thiện bảng kế hoạch đồ án nhóm chi tiết theo ngày.\n"
     "• Trương Quốc Anh Khoa: Kiểm tra chéo phân công nhiệm vụ, đối chiếu yêu cầu đề bài.\n"
     "• Bùi Ngọc Thiệu: Thiết lập kho mã nguồn chung trên Git/GitHub và Drive.",
     "File kế hoạch hoàn chỉnh, Repo Git của nhóm", "Hoàn thành"),
    ("Tuần 1", "Thứ 7",
     "• Cả nhóm (Phú, Khoa, Thiệu): Họp online tổng kết Tuần 1, duyệt kế hoạch và phân công Tuần 2.",
     "Biên bản nghiệm thu Tuần 1", "Hoàn thành"),

    # Tuần 2
    ("Tuần 2", "Thứ 2",
     "• Nguyễn Minh Phú: Truy cập hệ thống https://cntttest.vanlanguni.edu.vn:18081/Phancong02/, kiểm tra quyền BCN Khoa.\n"
     "• Trương Quốc Anh Khoa: Thử nghiệm luồng giao diện người dùng vai trò BCN Khoa.\n"
     "• Bùi Ngọc Thiệu: Chụp màn hình trang chủ và thanh menu điều hướng BCN Khoa.",
     "Hình ảnh giao diện trang chủ BCN Khoa", "Hoàn thành"),
    ("Tuần 2", "Thứ 3",
     "• Nguyễn Minh Phú: Khảo sát chi tiết Module Quản lý Người dùng (User Management).\n"
     "• Trương Quốc Anh Khoa: Khảo sát chi tiết Module Quản lý Học kỳ (Term) và Ngành (Major).\n"
     "• Bùi Ngọc Thiệu: Khảo sát chi tiết Module Thời khóa biểu (Import, Export, Phân công).",
     "Ghi chú luồng hoạt động từng Module", "Hoàn thành"),
    ("Tuần 2", "Thứ 4",
     "• Nguyễn Minh Phú: Lập danh sách các phần tử HTML (ID, Name, XPath) của Module User.\n"
     "• Trương Quốc Anh Khoa: Liệt kê các trường dữ liệu bắt buộc của Module Term và Major.\n"
     "• Bùi Ngọc Thiệu: Khảo sát giao diện Thống kê và Bảng tính thù lao giảng dạy.",
     "Bảng danh mục Element Locators sơ bộ", "Hoàn thành"),
    ("Tuần 2", "Thứ 5",
     "• Nguyễn Minh Phú: Phân loại các chức năng có thể tự động hóa vs kiểm thử thủ công.\n"
     "• Trương Quốc Anh Khoa: Tổng hợp danh sách chức năng BCN Khoa đưa vào báo cáo Word.\n"
     "• Bùi Ngọc Thiệu: Chụp toàn bộ ảnh giao diện từng chức năng BCN Khoa.",
     "Bộ ảnh chụp màn hình UI đầy đủ của BCN Khoa", "Hoàn thành"),
    ("Tuần 2", "Thứ 6",
     "• Nguyễn Minh Phú: Soạn thảo nội dung Phần 1 & Phần 2 của Báo cáo đồ án Tuần 2.\n"
     "• Trương Quốc Anh Khoa: Đối chiếu danh sách chức năng với Product Backlog để đảm bảo không sót.\n"
     "• Bùi Ngọc Thiệu: Chèn và căn chỉnh hình ảnh chụp màn hình UI vào file Word.",
     "Bản thảo Báo cáo đồ án Tuần 2", "Hoàn thành"),
    ("Tuần 2", "Thứ 7",
     "• Cả nhóm: Họp online nghiệm thu kết quả khảo sát Tuần 2, hoàn thiện gói nộp bài Tuần 2.",
     "Báo cáo Tuần 2 hoàn chỉnh (Team06_Ver1.1.docx)", "Hoàn thành")
]

tbl_prog = doc.add_table(rows=1, cols=len(sched_headers))
tbl_prog.alignment = WD_TABLE_ALIGNMENT.CENTER
for c_i, h in enumerate(sched_headers):
    format_cell(tbl_prog.rows[0].cells[c_i], h, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, fill_hex="003366", text_color="FFFFFF")

for row_data in progress_rows:
    r_cells = tbl_prog.add_row().cells
    for c_i, val in enumerate(row_data):
        is_bold = (c_i in [0, 1, 3, 4])
        align = WD_ALIGN_PARAGRAPH.CENTER if c_i in [0, 1, 4] else WD_ALIGN_PARAGRAPH.LEFT
        fill_bg = "E2EFDA" if c_i == 4 else None
        txt_col = "375623" if c_i == 4 else "000000"
        format_cell(r_cells[c_i], val, bold=is_bold, align=align, fill_hex=fill_bg, text_color=txt_col)

# Col widths
col_w = [Inches(0.7), Inches(0.6), Inches(3.6), Inches(1.4), Inches(0.8)]
for r in tbl_prog.rows:
    for c_i, w in enumerate(col_w):
        r.cells[c_i].width = w

add_heading_2("1.3. Đánh giá kết quả đạt được sau 2 tuần")
add_body(
    "• Tiến độ hoàn thành: Đạt 100% kế hoạch đề ra cho Tuần 1 và Tuần 2.\n"
    "• Sản phẩm đầu ra: Bản kế hoạch công việc chi tiết (Word & Excel), danh sách phân loại chức năng BCN Khoa và trọn bộ ảnh chụp giao diện hệ thống thực tế.\n"
    "• Tinh thần làm việc nhóm: Cả 3 thành viên tham gia tích cực, họp đúng lịch vào tối Thứ 7 hằng tuần."
)

# -------------------------------------------------------------
# PHẦN 2: KHẢO SÁT HỆ THỐNG VÀ PHẠM VI NGHIỆP VỤ BCN KHOA
# -------------------------------------------------------------
add_heading_1("PHẦN 2: KHẢO SÁT HỆ THỐNG VÀ PHẠM VI NGHIỆP VỤ BCN KHOA")

add_heading_2("2.1. Tổng quan hệ thống Quản lý phân công giảng dạy")
add_body(
    "Phần mềm 'Quản lý phân công giảng dạy' được phát triển phục vụ công tác quản lý của Khoa Công nghệ Thông tin - Trường Đại học Văn Lang. "
    "Hệ thống vận hành trên nền tảng Web tại địa chỉ: https://cntttest.vanlanguni.edu.vn:18081/Phancong02/.\n"
    "Hệ thống hỗ trợ 3 nhóm đối tượng người dùng chính:\n"
    "1. Ban chủ nhiệm Khoa (Faculty Board): Quản trị toàn bộ dữ liệu người dùng, học kỳ, ngành học, thời khóa biểu, thống kê và thù lao.\n"
    "2. Phụ trách bộ môn (Department Head): Theo dõi và phân công giảng viên giảng dạy các môn học thuộc bộ môn quản lý.\n"
    "3. Giảng viên (Lecturer): Theo dõi thời khóa biểu cá nhân, thống kê số giờ dạy và định mức thù lao."
)

add_heading_2("2.2. Phạm vi kiểm thử (Scope) được giao cho nhóm")
add_body(
    "Căn cứ yêu cầu tại Mục 2.b trong tài liệu FinalAssignment 1: 'Chỉ lấy những chức năng của vai trò BCN Khoa (Faculty Board)'.\n"
    "Do đó, nhóm kiểm thử Team 06 tập trung nghiên cứu, thiết kế test case và lập trình kịch bản tự động hóa chuyên biệt cho BCN Khoa, "
    "không thực hiện kiểm thử các chức năng dành riêng cho Trưởng bộ môn hoặc Giảng viên."
)

# -------------------------------------------------------------
# PHẦN 3: DANH SÁCH CHỨC NĂNG BCN KHOA CÓ THỂ TỰ ĐỘNG HÓA
# -------------------------------------------------------------
add_heading_1("PHẦN 3: DANH SÁCH CHỨC NĂNG BCN KHOA CÓ THỂ TỰ ĐỘNG HÓA KIỂM THỬ")

add_body(
    "Sau khi khảo sát tài liệu FunctionList_V1.8.xlsx, ProductBacklog.xlsx và trực tiếp trải nghiệm phần mềm, "
    "nhóm đã phân tích và lập danh sách chi tiết các chức năng của BCN Khoa có thể áp dụng kiểm thử tự động (Automation Testing):"
)

fn_headers = ["STT", "Mã CN", "Tên chức năng", "Mô tả nghiệp vụ", "Độ ưu tiên", "Khả năng Auto", "Kịch bản test tự động đề xuất"]
fn_data = [
    (1, "F.1.1", "Đăng nhập / Đăng xuất", "Đăng nhập bằng tài khoản email VLU phân quyền BCN Khoa và đăng xuất", "High", "Có", "Kiểm thử login thành công, login sai mật khẩu, tài khoản không hợp lệ, logout."),
    (2, "F.2.1", "Xem danh sách người dùng", "Xem bảng danh sách người dùng, giảng viên trong hệ thống", "Medium", "Có", "Kiểm thử tải bảng dữ liệu, phân trang, hiển thị đúng thông tin cột."),
    (3, "F.2.2", "Thêm người dùng mới", "Thêm giảng viên/người dùng mới kèm phân quyền trong Khoa", "High", "Có", "Kiểm thử tạo user thành công, kiểm thử validation để trống, trùng mã GV/email."),
    (4, "F.2.3", "Cập nhật người dùng", "Chỉnh sửa thông tin cá nhân, phân quyền của người dùng", "High", "Có", "Kiểm thử cập nhật họ tên, vai trò, số điện thoại, kiểm tra lưu thành công."),
    (5, "F.2.4", "Xóa người dùng", "Xóa tài khoản người dùng khỏi hệ thống", "High", "Có", "Kiểm thử bấm xóa, xác nhận popup dialog confirm xóa, kiểm tra user biến mất."),
    (6, "F.2.5", "Tìm kiếm người dùng", "Tìm kiếm người dùng theo tên, mã giảng viên hoặc email", "Medium", "Có", "Kiểm thử nhập từ khóa hợp lệ, từ khóa không tồn tại, kiểm tra kết quả lọc."),
    (7, "F.2.6", "Khóa tài khoản", "Khóa tài khoản giảng viên đã nghỉ hoặc chuyển công tác", "Medium", "Có", "Kiểm thử đổi trạng thái Active sang Locked, xác nhận user không login được."),
    (8, "F.3.1", "Xem danh sách học kỳ", "Xem bảng tổng hợp các học kỳ trong năm", "Medium", "Có", "Kiểm thử hiển thị danh sách học kỳ, kiểm tra thứ tự sắp xếp."),
    (9, "F.3.2", "Tạo học kỳ mới", "Tạo học kỳ mới (Mã HK, Tên HK, ngày bắt đầu, ngày kết thúc)", "High", "Có", "Kiểm thử tạo HK hợp lệ, kiểm thử trùng mã HK, ngày kết thúc trước ngày bắt đầu."),
    (10, "F.3.3", "Cập nhật học kỳ", "Chỉnh sửa thông tin học kỳ đã tạo", "High", "Có", "Kiểm thử sửa tên học kỳ, đổi ngày kết thúc, kiểm tra lưu thành công."),
    (11, "F.3.4", "Xóa học kỳ", "Xóa học kỳ chưa phát sinh dữ liệu thời khóa biểu", "High", "Có", "Kiểm thử xóa học kỳ rác, kiểm tra thông báo không cho xóa nếu đã có TKB."),
    (12, "F.3.5", "Tìm kiếm học kỳ", "Tìm kiếm học kỳ theo tên hoặc mã", "Medium", "Có", "Kiểm thử lọc học kỳ theo từ khóa năm học."),
    (13, "F.3.6", "Khóa học kỳ", "Khóa học kỳ để ngăn chặn chỉnh sửa sau khi đã chốt dữ liệu", "High", "Có", "Kiểm thử khóa HK, verify các nút sửa/xóa TKB bị vô hiệu hóa."),
    (14, "F.4.1-F.4.5", "Quản lý Ngành học", "Xem danh sách, Thêm, Sửa, Xóa và Tìm kiếm ngành học", "Medium", "Có", "Kiểm thử trọn bộ CRUD ngành học (CNTT, KTPM, MMT...), kiểm tra validation."),
    (15, "F.5.1", "Import thời khóa biểu", "Tải lên tệp Excel thời khóa biểu từ Phòng Đào tạo", "High", "Có", "Kiểm thử upload tệp Excel chuẩn, tệp sai định dạng, tệp rỗng bằng sendKeys."),
    (16, "F.5.2", "Export thời khóa biểu", "Xuất file Excel TKB đã phân công để gửi Phòng Đào tạo", "High", "Có", "Kiểm thử nhấp nút Export, verify tệp Excel được tải về thư mục Downloads."),
    (17, "F.5.3", "Xem TKB toàn khoa", "Xem bảng TKB toàn khoa theo tuần và theo giảng viên", "Medium", "Có", "Kiểm thử lọc theo tuần, chuyển đổi giữa chế độ xem tuần và học kỳ."),
    (18, "F.5.4", "Phân công giảng viên", "Chọn giảng viên phụ trách cho từng lớp học phần trên TKB", "High", "Có", "Kiểm thử chọn giảng viên từ Dropdown, kiểm tra cảnh báo trùng lịch dạy."),
    (19, "F.5.5", "Xóa lớp học phần", "Xóa lớp học phần thừa hoặc bị hủy trên TKB", "Medium", "Có", "Kiểm thử xóa lớp HP, kiểm tra lớp biến mất khỏi bảng TKB."),
    (20, "F.6.1-F.6.3", "Quản lý Thống kê", "Thống kê số giờ dạy, số môn dạy theo học kỳ và năm", "Medium", "Có", "Kiểm thử bộ lọc học kỳ, kiểm tra số liệu tổng giờ dạy hiển thị đúng."),
    (21, "F.7.1-F.7.19", "Quản lý Thù lao", "Quản lý học hàm, học vị, hệ số thù lao và bảng tính tiền dạy", "Low", "Có", "Kiểm thử cập nhật hệ số thù lao, xem bảng tính lương giảng dạy theo công thức.")
]

tbl_fn = doc.add_table(rows=1, cols=len(fn_headers))
tbl_fn.alignment = WD_TABLE_ALIGNMENT.CENTER
for c_i, h in enumerate(fn_headers):
    format_cell(tbl_fn.rows[0].cells[c_i], h, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, fill_hex="003366", text_color="FFFFFF")

for row_data in fn_data:
    r_cells = tbl_fn.add_row().cells
    for c_i, val in enumerate(row_data):
        val_str = str(val)
        is_bold = (c_i in [0, 1, 4])
        align = WD_ALIGN_PARAGRAPH.CENTER if c_i in [0, 1, 4, 5] else WD_ALIGN_PARAGRAPH.LEFT
        fill_bg = "F2F5F8" if row_data[0] % 2 == 0 else None
        format_cell(r_cells[c_i], val_str, bold=is_bold, align=align, fill_hex=fill_bg)

col_fn_w = [Inches(0.4), Inches(0.8), Inches(1.4), Inches(1.8), Inches(0.7), Inches(0.6), Inches(1.8)]
for r in tbl_fn.rows:
    for c_i, w in enumerate(col_fn_w):
        r.cells[c_i].width = w

doc.add_page_break()

# -------------------------------------------------------------
# PHẦN 4: HÌNH ẢNH GIAO DIỆN CÁC CHỨC NĂNG (KÈM SCREENSHOTS)
# -------------------------------------------------------------
add_heading_1("PHẦN 4: HÌNH ẢNH GIAO DIỆN CÁC CHỨC NĂNG BCN KHOA (UI SCREENSHOTS)")

add_body(
    "Dưới đây là hình ảnh chụp màn hình giao diện thực tế của từng phân hệ chức năng vai trò BCN Khoa, "
    "được trích xuất từ quá trình khảo sát và tài liệu hướng dẫn sử dụng của hệ thống:"
)

img_dir = r"D:\ktdt\Do an nhom\ui_images"

def embed_screenshot(img_file, caption_text, width=Inches(5.8)):
    img_path = os.path.join(img_dir, img_file)
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(6)
        p_img.paragraph_format.space_after = Pt(2)
        doc.add_picture(img_path, width=width)
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_after = Pt(10)
        r_cap = p_cap.add_run(caption_text)
        r_cap.italic = True
        r_cap.font.name = "Times New Roman"
        r_cap.font.size = Pt(9.5)
        r_cap.font.color.rgb = COLOR_GRAY

# 4.1 Login
add_heading_2("4.1. Phân hệ Đăng nhập / Đăng xuất (F.1.1)")
add_body(
    "Giao diện đăng nhập hệ thống Quản lý phân công giảng dạy. "
    "Người dùng vai trò BCN Khoa bấm nút 'Đăng nhập' để chuyển hướng sang cổng xác thực email Văn Lang (@vanlanguni.edu.vn)."
)
embed_screenshot("page_8_img_1.png", "Hình 1: Giao diện Trang chủ và Đăng nhập hệ thống bằng email VLU")

# 4.2 User Management
add_heading_2("4.2. Phân hệ Quản lý Người dùng (User Management - F.2.1 đến F.2.6)")
add_body(
    "Giao diện danh sách người dùng hiển thị bảng thông tin gồm: STT, Mã giảng viên, Họ và tên, Email, Phân quyền và Trạng thái. "
    "Các nút chức năng bao gồm: Thêm mới người dùng, Tìm kiếm, Sửa thông tin, Xóa và Khóa tài khoản."
)
embed_screenshot("page_11_img_1.png", "Hình 2: Giao diện Danh sách Người dùng trong Khoa (F.2.1)")

# 4.3 Term Management
add_heading_2("4.3. Phân hệ Quản lý Học kỳ (Term Management - F.3.1 đến F.3.6)")
add_body(
    "Giao diện Quản lý Học kỳ hiển thị danh sách các học kỳ theo từng năm học. "
    "BCN Khoa có thể thực hiện: Thêm học kỳ mới, Chỉnh sửa thời gian học kỳ, Xóa học kỳ và Khóa học kỳ."
)
embed_screenshot("page_22_img_1.png", "Hình 3: Giao diện Quản lý Học kỳ (F.3.1)")
embed_screenshot("page_23_img_1.png", "Hình 4: Giao diện Form Thêm mới Học kỳ (F.3.2)")

# 4.4 Major Management
add_heading_2("4.4. Phân hệ Quản lý Ngành học (Major Management - F.4.1 đến F.4.5)")
add_body(
    "Giao diện hiển thị danh sách các ngành đào tạo thuộc Khoa CNTT (Công nghệ thông tin, Kỹ thuật phần mềm, An toàn thông tin...). "
    "Hỗ trợ các thao tác Thêm, Sửa, Xóa và Tìm kiếm ngành học."
)
embed_screenshot("page_31_img_1.png", "Hình 5: Giao diện Quản lý Ngành học (F.4.1)")

# 4.5 Timetable Management
add_heading_2("4.5. Phân hệ Quản lý Thời khóa biểu (Timetable Management - F.5.1 đến F.5.6)")
add_body(
    "Giao diện Thời khóa biểu hiển thị lưới lịch học theo tuần và học kỳ. "
    "BCN Khoa thực hiện: Import file Excel TKB, Phân công giảng viên giảng dạy từ danh sách thả xuống, Xóa lớp học phần và Export TKB."
)
embed_screenshot("page_44_img_1.png", "Hình 6: Giao diện Bảng Thời khóa biểu và Phân công giảng viên (F.5.3 & F.5.4)")

# 4.6 Statistics & Remuneration
add_heading_2("4.6. Phân hệ Thống kê & Thù lao (Statistics & Remuneration - F.6 & F.7)")
add_body(
    "Giao diện thống kê giờ dạy thực tế của giảng viên theo học kỳ và năm học, đối chiếu với định mức quy định. "
    "Phân hệ thù lao quản lý hệ số giảng dạy, học hàm/học vị và bảng tính lương thù lao."
)
embed_screenshot("page_61_img_1.png", "Hình 7: Giao diện Thống kê số giờ dạy theo học kỳ (F.6.1)")
embed_screenshot("page_132_img_1.png", "Hình 8: Giao diện Quản lý Bảng tính Thù lao giảng dạy (F.7.19)")

# -------------------------------------------------------------
# PHẦN 5: KẾ HOẠCH TRIỂN KHAI TUẦN 3
# -------------------------------------------------------------
add_heading_1("PHẦN 5: KẾ HOẠCH CÔNG VIỆC TRỌNG TÂM CHO TUẦN 3")

add_body(
    "Bước sang Tuần 3, nhóm sẽ chuyển từ giai đoạn Khảo sát sang giai đoạn Thiết kế Kịch bản kiểm thử (Test Design):\n"
    "1. Nguyễn Minh Phú (Nhóm trưởng): Định hình mẫu biểu Test Case theo chuẩn IEEE 829; review và chuẩn hóa bộ Test Case cho Module Đăng nhập & Người dùng.\n"
    "2. Trương Quốc Anh Khoa: Viết kịch bản kiểm thử chi tiết (Test Cases) cho chức năng Đăng nhập (F.1.1) và Quản lý Người dùng (F.2.1, F.2.2, F.2.3, F.2.4).\n"
    "3. Bùi Ngọc Thiệu: Thiết kế Test Cases cho chức năng Tìm kiếm (F.2.5), Khóa tài khoản (F.2.6); chuẩn bị bộ dữ liệu kiểm thử (Test Data) gồm các tài khoản mẫu và thông tin giảng viên.\n"
    "4. Cả nhóm: Họp nghiệm thu vào tối Thứ 7 của Tuần 3 để chốt danh sách Test Cases chuẩn bị cho việc viết Automation Script ở Tuần 4 và Tuần 5."
)

# Signature block
p_sign = doc.add_paragraph()
p_sign.alignment = WD_ALIGN_PARAGRAPH.RIGHT
p_sign.paragraph_format.space_before = Pt(20)
r_sign = p_sign.add_run("TP. Hồ Chí Minh, ngày 12 tháng 10 năm 2026\nĐẠI DIỆN NHÓM (TRƯỞNG NHÓM)\n\n\n\nNguyễn Minh Phú")
r_sign.font.name = "Times New Roman"
r_sign.font.size = Pt(11)
r_sign.bold = True

# Save to docx files
out_path1 = r"D:\ktdt\Do an nhom\BaoCao_Tuan2_Team06.docx"
out_path2 = r"D:\ktdt\Do an nhom\Team06_Ver1.1.docx"

doc.save(out_path1)
doc.save(out_path2)
print("Successfully generated BaoCao_Tuan2_Team06.docx and Team06_Ver1.1.docx with embedded UI screenshots!")
