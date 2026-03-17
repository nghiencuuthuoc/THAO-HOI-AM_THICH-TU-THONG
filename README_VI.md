# THAO HỘI ÂM – THÍCH TỪ THÔNG

Bộ công cụ tổ chức dữ liệu và tải tài nguyên công khai của Thao Hội Âm liên quan đến Thích Từ Thông.

## Tổng quan

Repository này được xây dựng để hỗ trợ người dùng:

- tổ chức danh sách URL bài viết và chuyên mục,
- ánh xạ trang web sang cây thư mục cục bộ,
- tải các tệp tài liệu, âm thanh và video từ từng trang bài viết,
- lưu trữ dữ liệu một cách có cấu trúc để học tập, tra cứu và bảo tồn lâu dài.

Mục tiêu là tạo một quy trình dễ dùng cho người dùng cuối: thu thập URL trang, sinh mapping thư mục, và tải các tệp không phải tài nguyên web như PDF, DOC, MP3 và video.

## Các tệp chính trong dự án

Thông thường dự án sẽ có các tệp sau:

- `download_thaohoiam_assets.py`  
  Script tải các tệp hỗ trợ từ trang bài viết và bỏ qua các tài nguyên web như CSS, JS, HTML và ảnh giao diện.

- `requirements_thaohoiam_assets.txt`  
  Danh sách thư viện Python cần cài.

- `urls.txt`  
  Danh sách URL trang cần xử lý, mỗi dòng một URL.

- `_URL_MAP.csv`  
  Bảng ánh xạ giữa tiêu đề, tên thư mục, URL trang và đường dẫn đầu ra.

- `_URL_MAP.json`  
  Phiên bản JSON của bảng ánh xạ để thuận tiện cho tự động hóa.

## Loại tệp hỗ trợ tải

Script chỉ tập trung vào nội dung dữ liệu, không tải tài nguyên dựng website.

Ví dụ được hỗ trợ:

- Tài liệu: PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX, TXT, RTF, EPUB, CSV
- Âm thanh: MP3, WAV, M4A, FLAC, OGG, AAC
- Video: MP4, MKV, AVI, MOV, WEBM, MPEG

Ví dụ bị bỏ qua:

- HTML và các tệp trang web
- CSS và JavaScript
- ảnh giao diện web phổ biến và font web

## Cách dùng nhanh

### 1. Cài thư viện Python

```bash
pip install -r requirements_thaohoiam_assets.txt
```

### 2. Tải từ một trang

```bash
python download_thaohoiam_assets.py --url "http://thaohoiam.vn/bat-nha-ba-la-mat-kinh/" --out "./THAO_HOI_AM_DOWNLOADS"
```

### 3. Tải từ nhiều URL

```bash
python download_thaohoiam_assets.py --url-file "urls.txt" --out "./THAO_HOI_AM_DOWNLOADS"
```

### 4. Tải từ file ánh xạ URL

```bash
python download_thaohoiam_assets.py --map-csv "_URL_MAP.csv" --out "./THAO_HOI_AM_DOWNLOADS"
```

## Cấu trúc đầu ra

Ví dụ thư mục kết quả:

```text
THAO_HOI_AM_DOWNLOADS/
├── BAT NHA BA LA MAT KINH/
│   ├── PAGE_URL.txt
│   ├── FOUND_FILE_URLS.txt
│   ├── FOUND_FILE_URLS.csv
│   ├── BAT-NHA.pdf
│   ├── BN-01.mp3
│   ├── BN-02.mp3
│   └── ...
├── _download_log.csv
└── _download_state.json
```

## Tính năng chính

- hỗ trợ tải tiếp khi chạy lại,
- bỏ qua tệp đã tải xong,
- tự thử lại khi lỗi mạng tạm thời,
- lưu danh sách URL tệp tìm thấy để kiểm tra,
- ghi log và trạng thái tải,
- tổ chức dữ liệu theo từng thư mục bài viết.

## Trường hợp sử dụng phù hợp

Repository này phù hợp cho:

- lưu trữ tài liệu học tập cá nhân,
- bảo tồn số các tài liệu học tập công khai,
- truy cập offline có cấu trúc,
- quản lý dữ liệu bằng script.

## Lưu ý quan trọng

- Chỉ tải các nội dung mà bạn có quyền truy cập và lưu trữ.
- Cần kiểm tra bản quyền, điều khoản sử dụng và quy định pháp lý địa phương trước khi tải hàng loạt.
- Một số tệp có thể được nhúng động và không xuất hiện trực tiếp trong HTML tĩnh của trang.
- Cần kiểm tra lại dữ liệu đã tải trước khi chia sẻ lại cho người khác.

## Gợi ý cấu trúc repository

```text
THAO-HOI-AM_THICH-TU-THONG/
├── download_thaohoiam_assets.py
├── requirements_thaohoiam_assets.txt
├── urls.txt
├── _URL_MAP.csv
├── _URL_MAP.json
├── README_EN.md
└── README_VI.md
```

## Trách nhiệm sử dụng

Hãy sử dụng repository này một cách có trách nhiệm. Người dùng tự chịu trách nhiệm kiểm tra quyền sử dụng nội dung, phạm vi cho phép của nguồn dữ liệu và các quy định pháp lý liên quan trước khi tải hoặc chia sẻ tệp.

---
© 2009-2026 • Pharma R&D Platforms • PharmApp • Discover • Design • Develop • Validate • Deliver | www.nghiencuuthuoc.com | Zalo:
+84888999311 | www.pharmapp.dev
