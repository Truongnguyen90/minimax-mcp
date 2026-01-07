# 🧪 Công Cụ Test MiniMax API Cho iPad

## 📖 Tài Liệu Hướng Dẫn

Repo này bao gồm các công cụ và hướng dẫn để test MiniMax API trên iPad và các thiết bị khác:

### 📄 Hướng Dẫn Chi Tiết

1. **[HUONG_DAN_IPAD.md](HUONG_DAN_IPAD.md)** - Hướng dẫn cài đặt MCP cho Claude
   - Giải thích MCP là gì và tại sao không hoạt động trên iPad
   - Hướng dẫn cài đặt trên Claude Desktop
   - Các phương án thay thế cho iPad

2. **[KIEM_TRA_IPAD.md](KIEM_TRA_IPAD.md)** - Hướng dẫn kiểm tra API ⭐ BẮT ĐẦU TỪ ĐÂY
   - Cách sử dụng công cụ test HTML
   - Cách sử dụng Python script
   - Xử lý lỗi thường gặp
   - FAQ chi tiết

### 🛠️ Công Cụ Test

1. **[test_ipad.html](test_ipad.html)** - Web-based API tester cho iPad
   - Mở trực tiếp trên iPad browser
   - Giao diện đẹp, dễ sử dụng
   - Hỗ trợ test nhiều API endpoints
   - Không cần cài đặt

2. **[test_api.py](test_api.py)** - Python script để test API
   - Chi tiết, có màu sắc
   - Hỗ trợ nhiều options
   - Thích hợp cho debugging
   - Chạy trên Mac/PC/Linux

3. **[claude_ipad_config.json](claude_ipad_config.json)** - File cấu hình mẫu
   - Template cho Claude Desktop
   - Đã điền sẵn cấu trúc
   - Chỉ cần thay API key

## 🚀 Bắt Đầu Nhanh

### Cho Người Dùng iPad

1. **Download file `test_ipad.html`**
2. **Mở trong Safari trên iPad**
3. **Nhập API Key** (lấy từ [MiniMax Platform](https://www.minimax.io/platform))
4. **Chọn API để test** và nhấn "Test API"

Xem hướng dẫn chi tiết: [KIEM_TRA_IPAD.md](KIEM_TRA_IPAD.md)

### Cho Người Dùng Mac/PC

#### Cách 1: Sử dụng HTML Tool
- Mở `test_ipad.html` trong browser
- Sử dụng tương tự như trên iPad

#### Cách 2: Sử dụng Python Script
```bash
# Cài đặt dependencies
pip install requests

# Chạy test
python test_api.py \
  --api-key YOUR_API_KEY \
  --api-host https://api.minimax.io
```

Xem hướng dẫn chi tiết: [KIEM_TRA_IPAD.md](KIEM_TRA_IPAD.md)

## ⚠️ Lưu Ý Quan Trọng

### MCP Không Hoạt Động Trên iPad

**MCP (Model Context Protocol)** chỉ hoạt động với:
- ✅ Claude Desktop (macOS/Windows)
- ✅ Cursor Editor
- ✅ Windsurf IDE
- ✅ Các MCP clients khác

**KHÔNG hoạt động với:**
- ❌ Claude app trên iPad/iPhone
- ❌ Claude web trên mobile browser

### Công Cụ Test Là Gì?

Các công cụ trong repo này giúp bạn:
- ✅ Test **API** của MiniMax (không phải MCP)
- ✅ Xác minh API Key hoạt động
- ✅ Kiểm tra kết nối
- ✅ Hiểu cách API hoạt động

## 📋 So Sánh Các Công Cụ

| Tính Năng | HTML Tool | Python Script |
|-----------|-----------|---------------|
| **Chạy trên iPad** | ✅ | ❌ |
| **Chạy trên Mac/PC** | ✅ | ✅ |
| **Không cần cài đặt** | ✅ | ❌ (cần Python) |
| **Giao diện đẹp** | ✅ | ❌ (CLI) |
| **Chi tiết kỹ thuật** | ⚠️ Cơ bản | ✅ Rất chi tiết |
| **Phát audio trực tiếp** | ✅ | ❌ |
| **Automation** | ❌ | ✅ |

**Khuyến nghị:**
- 🎨 Dùng **HTML tool** cho test nhanh và demo
- 🔧 Dùng **Python script** cho debugging và automation

## 🔑 Lấy API Key

### Global (Quốc Tế)
- 🌍 Platform: https://www.minimax.io/platform
- 🔑 API Key: https://www.minimax.io/platform/user-center/basic-information/interface-key
- 🌐 API Host: `https://api.minimax.io`

### China (Trung Quốc)
- 🌍 Platform: https://platform.minimaxi.com
- 🔑 API Key: https://platform.minimaxi.com/user-center/basic-information/interface-key
- 🌐 API Host: `https://api.minimaxi.com`

⚠️ **API Key và Host phải cùng khu vực!**

## 🎯 Các API Có Thể Test

| API | Miễn Phí? | HTML Tool | Python Script |
|-----|-----------|-----------|---------------|
| List Voices | ✅ Miễn phí | ✅ | ✅ |
| Text to Speech | ⚠️ Tốn phí | ✅ | ✅ |
| Voice Clone | ⚠️ Tốn phí | ❌ | Sắp có |
| Video Generation | ⚠️ Tốn phí | ⚠️ Query only | Sắp có |
| Image Generation | ⚠️ Tốn phí | ❌ | Sắp có |
| Music Generation | ⚠️ Tốn phí | ❌ | Sắp có |

## 🐛 Gặp Vấn Đề?

1. **Đọc FAQ:** [KIEM_TRA_IPAD.md → FAQ](KIEM_TRA_IPAD.md#-faq)
2. **Xử lý lỗi:** [KIEM_TRA_IPAD.md → Xử Lý Lỗi](KIEM_TRA_IPAD.md#-xử-lý-lỗi-thường-gặp)
3. **Tạo Issue:** [GitHub Issues](https://github.com/MiniMax-AI/MiniMax-MCP/issues)

## 🎓 Muốn Dùng MCP Đầy Đủ?

Xem hướng dẫn cài đặt MCP cho Claude Desktop:
- [HUONG_DAN_IPAD.md](HUONG_DAN_IPAD.md)

## 📚 Tài Liệu Liên Quan

- [README.md](README.md) - Hướng dẫn chính của MiniMax MCP
- [README-CN.md](README-CN.md) - Hướng dẫn tiếng Trung
- [MiniMax API Docs](https://www.minimax.io/docs) - API documentation

## 🤝 Đóng Góp

Đóng góp luôn được chào đón! Nếu bạn có ý tưởng cải thiện công cụ test:
1. Fork repo này
2. Tạo branch mới
3. Commit changes
4. Tạo Pull Request

## 📄 License

MIT License - Xem [LICENSE](LICENSE) để biết chi tiết.

---

**Chúc bạn test thành công! 🎉**

Nếu có câu hỏi, hãy tạo issue hoặc tham gia cộng đồng MiniMax.
