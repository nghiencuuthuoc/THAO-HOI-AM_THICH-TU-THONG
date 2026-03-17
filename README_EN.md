# THAO HOI AM – THICH TU THONG

A structured preservation and download toolkit for public Thao Hoi Am resources related to Thích Từ Thông.

## Overview

This repository is intended to help users:

- organize article and category URLs,
- map website pages to local folders,
- download supported document, audio, and video files from article pages,
- keep a clean and reproducible archive for research, study, and long-term preservation.

The repository is designed for practical end users who want a simple workflow: collect page URLs, generate folder mappings, and download non-web assets such as PDF, DOC, MP3, and video files.

## Included Files

Typical files in this project include:

- `download_thaohoiam_assets.py`  
  Downloads supported files from article pages while skipping web assets such as CSS, JS, HTML, and site images.

- `requirements_thaohoiam_assets.txt`  
  Python dependencies for the downloader.

- `urls.txt`  
  A plain text list of page URLs to process.

- `_URL_MAP.csv`  
  A mapping file between titles, folder names, page URLs, and output paths.

- `_URL_MAP.json`  
  JSON version of the URL mapping for easier automation and scripting.

## Supported Download Types

The downloader is designed for non-web content only.

Supported examples:

- Documents: PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX, TXT, RTF, EPUB, CSV
- Audio: MP3, WAV, M4A, FLAC, OGG, AAC
- Video: MP4, MKV, AVI, MOV, WEBM, MPEG

Skipped examples:

- HTML and other webpage files
- CSS and JavaScript
- common web images and web fonts used for site rendering

## Quick Start

### 1. Install Python packages

```bash
pip install -r requirements_thaohoiam_assets.txt
```

### 2. Download from one page

```bash
python download_thaohoiam_assets.py --url "http://thaohoiam.vn/bat-nha-ba-la-mat-kinh/" --out "./THAO_HOI_AM_DOWNLOADS"
```

### 3. Download from many page URLs

```bash
python download_thaohoiam_assets.py --url-file "urls.txt" --out "./THAO_HOI_AM_DOWNLOADS"
```

### 4. Download from the URL map

```bash
python download_thaohoiam_assets.py --map-csv "_URL_MAP.csv" --out "./THAO_HOI_AM_DOWNLOADS"
```

## Output Structure

A typical output folder may look like this:

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

## Main Features

- resume-friendly downloading,
- skip files already downloaded,
- retry on temporary network failures,
- save found file URLs for review,
- keep logs and download state,
- organize outputs by page folder.

## Recommended Use

This repository is suitable for:

- personal study archives,
- digital preservation of public learning materials,
- structured offline access,
- script-based collection management.

## Important Notes

- Only download content that you are allowed to access and store.
- Review copyright, terms of use, and local legal requirements before bulk downloading.
- Some files may be embedded dynamically and may not be visible in static page HTML.
- Always verify downloaded materials before redistribution.

## Suggested Repository Structure

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

## License and Responsibility

Use this repository responsibly. The user is responsible for checking usage rights, content permissions, and applicable laws before downloading or sharing files.

---
© 2009-2026 • Pharma R&D Platforms • PharmApp • Discover • Design • Develop • Validate • Deliver | www.nghiencuuthuoc.com | Zalo:
+84888999311 | www.pharmapp.dev
