from pathlib import Path
import csv, json, re, unicodedata, zipfile
from bs4 import BeautifulSoup

HTML_SNIPPET = r'''
<li id="cat-item-3" class="cat-item has_parent exp"><a href="http://thaohoiam.vn/chuyen-muc/kinh-dai-thua/"><span class="cat-icon cat-icon-minus"></span><span class="text-link">Kinh Đại Thừa (43)</span></a><ul class="nav nav-pills children" style="display: block;"><li id="cat-item-18" class="cat-item has_parent"><a href="http://thaohoiam.vn/chuyen-muc/kinh-dai-thua/8-bo-kinh-dai-thua/"><span class="cat-icon cat-icon-plus"></span><span class="text-link">8 bộ kinh Đại Thừa (9)</span></a><ul class="nav nav-pills children"><li id="post-item-128" class="post-item"><a href="http://thaohoiam.vn/bat-nha-ba-la-mat-kinh/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Bát Nhã Ba La Mật Kinh</span></a></li><li id="post-item-3198" class="post-item"><a href="http://thaohoiam.vn/dao-trang-bat-nha/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Bát Nhã Đạo Tràng</span></a></li><li id="post-item-1" class="post-item"><a href="http://thaohoiam.vn/chung-dao-ca/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Chứng Đạo Ca</span></a></li><li id="post-item-132" class="post-item"><a href="http://thaohoiam.vn/duy-ma-cat-kinh/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Duy Ma Cật kinh</span></a></li><li id="post-item-119" class="post-item"><a href="http://thaohoiam.vn/duy-thuc-hoc/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Duy Thức Học</span></a></li><li id="post-item-130" class="post-item"><a href="http://thaohoiam.vn/dai-bat-niet-ban-kinh/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Đại Bát Niết Bàn kinh</span></a></li><li id="post-item-123" class="post-item"><a href="http://thaohoiam.vn/nhu-lai-vien-giac-kinh/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Như Lai Viên Giác kinh</span></a></li><li id="post-item-126" class="post-item"><a href="http://thaohoiam.vn/phap-hoa-kinh/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Pháp Hoa kinh</span></a></li><li id="post-item-121" class="post-item"><a href="http://thaohoiam.vn/thu-lang-nghiem-kinh/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Thủ Lăng Nghiêm kinh</span></a></li></ul></li><li id="cat-item-19" class="cat-item has_parent"><a href="http://thaohoiam.vn/chuyen-muc/kinh-dai-thua/trich-doan-8-bo-kinh/"><span class="cat-icon cat-icon-plus"></span><span class="text-link">Phật Học Vấn Đáp (14)</span></a><ul class="nav nav-pills children"><li id="post-item-2931" class="post-item"><a href="http://thaohoiam.vn/suy-gam/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Suy Gẫm</span></a></li><li id="post-item-144" class="post-item"><a href="http://thaohoiam.vn/bat-nha-ba-la-mat-kinh-2/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Vấn Đáp Bát Nhã Ba La Mật kinh</span></a></li><li id="post-item-3204" class="post-item"><a href="http://thaohoiam.vn/van-dap-dao-trang-bat-nha/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Vấn Đáp Bát Nhã Đạo Tràng</span></a></li><li id="post-item-134" class="post-item"><a href="http://thaohoiam.vn/van-dap-chung-dao-ca/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Vấn Đáp Chứng Đạo Ca</span></a></li><li id="post-item-5274" class="post-item"><a href="http://thaohoiam.vn/van-dap-duy-ma-cat-kinh/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Vấn đáp Duy Ma cật kinh</span></a></li><li id="post-item-136" class="post-item"><a href="http://thaohoiam.vn/duy-thuc-hoc-2/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Vấn Đáp Duy Thức Học</span></a></li><li id="post-item-5889" class="post-item"><a href="http://thaohoiam.vn/van-dap-dai-bat-niet-ban-kinh-tap-1/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Vấn đáp Đại Bát Niết Bàn kinh tập 1</span></a></li><li id="post-item-146" class="post-item"><a href="http://thaohoiam.vn/dai-bat-niet-ban-kinh-2/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Vấn đáp Đại Bát Niết Bàn kinh tập 2</span></a></li><li id="post-item-4522" class="post-item"><a href="http://thaohoiam.vn/van-dap-bai-giang-tang-ni-tai-truong-ph-tp-hcm/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Vấn đáp HD Tăng Ni tại trường Phật Học Tp. HCM</span></a></li><li id="post-item-4610" class="post-item"><a href="http://thaohoiam.vn/van-dap-nhu-huyen-thien-su-thi-tap/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Vấn đáp Như Huyễn Thiền Sư thi tập</span></a></li><li id="post-item-5131" class="post-item"><a href="http://thaohoiam.vn/van-dap-nhu-lai-vien-giac-kinh/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Vấn đáp Như Lai Viên Giác kinh</span></a></li><li id="post-item-142" class="post-item"><a href="http://thaohoiam.vn/phap-hoa-kinh-2/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Vấn Đáp Pháp Hoa kinh</span></a></li><li id="post-item-138" class="post-item"><a href="http://thaohoiam.vn/thu-lang-nghiem-kinh-2/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Vấn Đáp Thủ Lăng Nghiêm kinh</span></a></li><li id="post-item-3864" class="post-item"><a href="http://thaohoiam.vn/van-dap-cac-bai-giang-truong-ha/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Vấn Đáp-Các bài giảng trường hạ</span></a></li></ul></li><li id="cat-item-21" class="cat-item has_parent"><a href="http://thaohoiam.vn/chuyen-muc/kinh-dai-thua/cac-bai-giang-khac/"><span class="cat-icon cat-icon-plus"></span><span class="text-link">Các bài giảng khác (19)</span></a><ul class="nav nav-pills children"><li id="post-item-150" class="post-item"><a href="http://thaohoiam.vn/a-di-da-kinh/"><span class="cat-icon cat-icon-join"></span><span class="text-link">A Di Đà kinh</span></a></li><li id="post-item-4190" class="post-item"><a href="http://thaohoiam.vn/bai-giang-tang-ni-2014-tai-truong-ph-tp-hcm/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Bài Giảng Tăng Ni 2014 tại Trường PH Tp. HCM</span></a></li><li id="post-item-157" class="post-item"><a href="http://thaohoiam.vn/bat-dai-nhan-giac-kinh/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Bát Đại Nhân Giác kinh</span></a></li><li id="post-item-159" class="post-item"><a href="http://thaohoiam.vn/dai-thua-vo-luong-nghia-kinh/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Đại Thừa Vô Lượng Nghĩa kinh</span></a></li><li id="post-item-320" class="post-item"><a href="http://thaohoiam.vn/dia-tang-trich-nhu-huyen-thien-su-thi-tap/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Địa Tạng ( Trích NHTS thi tập)</span></a></li><li id="post-item-161" class="post-item"><a href="http://thaohoiam.vn/cac-bai-giang-chua-thien-minh/"><span class="cat-icon cat-icon-join"></span><span class="text-link">HDTH tại trường Phật học TP.HCM</span></a></li><li id="post-item-2729" class="post-item"><a href="http://thaohoiam.vn/loi-nhac-nho-hoc-phat-tai-truong-ph-tp-hcm/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Lời Nhắc Nhở Học Phật tại Trường PH Tp HCM</span></a></li><li id="post-item-163" class="post-item"><a href="http://thaohoiam.vn/xuan-suy-ngam/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Ngày xuân suy gẫm</span></a></li><li id="post-item-328" class="post-item"><a href="http://thaohoiam.vn/ngu-thua-phat-giao/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Ngũ Thừa Phật Giáo</span></a></li><li id="post-item-324" class="post-item"><a href="http://thaohoiam.vn/quan-the-am-trich-nhu-huyen-thien-su-thi-tap-2/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Quán Thế Âm (Trích NHTS thi tập)</span></a></li><li id="post-item-1999" class="post-item"><a href="http://thaohoiam.vn/quy-son-canh-sach-3/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Quy Sơn Cảnh Sách</span></a></li><li id="post-item-356" class="post-item"><a href="http://thaohoiam.vn/thap-nhi-nhan-duyen/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Tam Bảo Học</span></a></li><li id="post-item-248" class="post-item"><a href="http://thaohoiam.vn/tu-dieu-de-trich-ngon-tay-chi-trang-3/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Tứ Diệu Đế (Trích NTCT 3)</span></a></li><li id="post-item-1882" class="post-item"><a href="http://thaohoiam.vn/tu-phuoc-tu-tue/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Tu Phước - Tu Tuệ</span></a></li><li id="post-item-246" class="post-item"><a href="http://thaohoiam.vn/tu-thanh-de-trich-dai-bat-niet-ban-kinh/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Tứ Thánh Đế (Trích ĐBNB kinh)</span></a></li><li id="post-item-165" class="post-item"><a href="http://thaohoiam.vn/quy-son-canh-sach/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Tứ Thập Nhị Chương</span></a></li><li id="post-item-152" class="post-item"><a href="http://thaohoiam.vn/van-de-sinh-tu/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Vấn đề sanh tử</span></a></li><li id="post-item-154" class="post-item"><a href="http://thaohoiam.vn/xu-ly-van-de-sanh-tu/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Xử lý vấn đề sanh tử</span></a></li><li id="post-item-2701" class="post-item"><a href="http://thaohoiam.vn/y-nghia-tam-gioi-trong-dao-phat/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Ý Nghĩa Tam Giới Trong Đạo Phật</span></a></li></ul></li><li id="post-item-3836" class="post-item"><a href="http://thaohoiam.vn/cac-bai-giang-truong-ha/"><span class="cat-icon cat-icon-join"></span><span class="text-link">Các Bài Giảng Trường Hạ</span></a></li></ul></li>
'''

ROOT_NAME = "THAO_HOI_AM_TREE"
OUT_DIR = Path('/mnt/data')


def remove_accents(text: str) -> str:
    text = text.replace('đ', 'd').replace('Đ', 'D')
    text = unicodedata.normalize('NFD', text)
    text = ''.join(ch for ch in text if unicodedata.category(ch) != 'Mn')
    return unicodedata.normalize('NFC', text)


def clean_title(text: str) -> str:
    text = re.sub(r'\s*\(\d+\)\s*$', '', text.strip())
    return re.sub(r'\s+', ' ', text)


def normalize_folder_name(text: str) -> str:
    text = clean_title(text)
    text = remove_accents(text)
    text = text.upper()
    text = re.sub(r'[<>:"/\\|?*]', ' ', text)
    text = re.sub(r'[–—\-]+', ' ', text)
    text = re.sub(r"[.,;:!?()\[\]{}'\"`~@#$%^&+=]+", ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text or 'UNTITLED'


def get_direct_text_link(a_tag):
    text_link = a_tag.find('span', class_='text-link')
    if text_link:
        return text_link.get_text(' ', strip=True)
    return a_tag.get_text(' ', strip=True)


records = []
post_urls = []

def parse_li_node(li_tag, parent_parts):
    classes = li_tag.get('class', [])
    a_tag = li_tag.find('a', recursive=False)
    if not a_tag:
        return

    raw_title = get_direct_text_link(a_tag)
    title = clean_title(raw_title)
    url = (a_tag.get('href') or '').strip()
    node_type = 'category' if 'cat-item' in classes else 'post'
    folder_name = normalize_folder_name(title)
    current_parts = parent_parts + [folder_name]
    folder_path = '/'.join(current_parts)
    parent_folder = '/'.join(parent_parts) if parent_parts else ''

    rec = {
        'type': node_type,
        'title': title,
        'folder_name': folder_name,
        'url': url,
        'folder_path': folder_path,
        'parent_folder': parent_folder,
    }
    records.append(rec)
    if node_type == 'post' and url:
        post_urls.append(url)

    child_ul = li_tag.find('ul', class_='children', recursive=False)
    if child_ul:
        for child_li in child_ul.find_all('li', recursive=False):
            parse_li_node(child_li, current_parts)


soup = BeautifulSoup(f'<ul>{HTML_SNIPPET}</ul>', 'html.parser')
root_ul = soup.find('ul')
for top_li in root_ul.find_all('li', recursive=False):
    parse_li_node(top_li, [ROOT_NAME])

# write urls.txt with unique post URLs in snippet order
seen = set()
ordered_urls = []
for u in post_urls:
    if u not in seen:
        seen.add(u)
        ordered_urls.append(u)

(OUT_DIR / 'urls.txt').write_text('\n'.join(ordered_urls) + '\n', encoding='utf-8')

with (OUT_DIR / '_URL_MAP.csv').open('w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=['type','title','folder_name','url','folder_path','parent_folder'])
    writer.writeheader()
    writer.writerows(records)

(OUT_DIR / '_URL_MAP.json').write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8')

readme = OUT_DIR / 'README_THAOHOIAM_FILES.txt'
readme.write_text(
    'Included files:\n'
    '- download_thaohoiam_assets.py\n'
    '- requirements_thaohoiam_assets.txt\n'
    '- urls.txt\n'
    '- _URL_MAP.csv\n'
    '- _URL_MAP.json\n'
    '- make_thaohoiam_files.py\n',
    encoding='utf-8'
)

zip_path = OUT_DIR / 'thaohoiam_bundle.zip'
with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
    for name in [
        'download_thaohoiam_assets.py',
        'requirements_thaohoiam_assets.txt',
        'urls.txt',
        '_URL_MAP.csv',
        '_URL_MAP.json',
        'README_THAOHOIAM_FILES.txt',
        'make_thaohoiam_files.py',
    ]:
        p = OUT_DIR / name
        if p.exists():
            zf.write(p, arcname=name)

print('Created files:')
for name in ['urls.txt', '_URL_MAP.csv', '_URL_MAP.json', 'README_THAOHOIAM_FILES.txt', 'make_thaohoiam_files.py', 'thaohoiam_bundle.zip']:
    print(OUT_DIR / name)
print(f'Records: {len(records)}')
print(f'Post URLs: {len(ordered_urls)}')
