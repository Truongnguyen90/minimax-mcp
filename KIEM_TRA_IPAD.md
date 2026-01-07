# Hướng Dẫn Kiểm Tra MiniMax API Trên iPad

## ⚠️ Lưu Ý Quan Trọng

**MCP (Model Context Protocol) KHÔNG hoạt động trực tiếp trên iPad** vì:

- ❌ Claude app trên iPad không hỗ trợ MCP servers
- ❌ Claude web trên iPad không hỗ trợ MCP servers
- ✅ MCP chỉ hoạt động với Claude Desktop (macOS/Windows), Cursor, Windsurf, v.v.

**Tuy nhiên**, bạn vẫn có thể **kiểm tra API của MiniMax** hoạt động từ iPad bằng các công cụ test được cung cấp.

---

## 🎯 Mục Đích Của Các Công Cụ Test

Các công cụ trong repo này giúp bạn:

1. ✅ Xác minh API Key của bạn hoạt động đúng
2. ✅ Kiểm tra kết nối đến MiniMax API
3. ✅ Test các endpoints API khác nhau
4. ✅ Hiểu cách API hoạt động trước khi dùng với MCP

---

## 🛠️ Các Công Cụ Test Có Sẵn

### 1. Test HTML (Dùng Trên iPad Browser) ⭐ KHUYẾN NGHỊ

**File:** `test_ipad.html`

#### Cách Sử Dụng:

1. **Mở file HTML:**
   - Tải repo về máy có web server, hoặc
   - Upload file lên GitHub Pages, hoặc
   - Sử dụng service như [JSFiddle](https://jsfiddle.net/) để host

2. **Truy cập từ iPad:**
   - Mở file trong Safari hoặc Chrome trên iPad
   - Hoặc truy cập URL nếu bạn đã host online

3. **Nhập thông tin:**
   - **API Key**: Lấy từ [MiniMax Platform](https://www.minimax.io/platform/user-center/basic-information/interface-key)
   - **API Host**: Chọn khu vực phù hợp
     - Global: `https://api.minimax.io`
     - China: `https://api.minimaxi.com`

4. **Chọn API để test:**
   - **List Voices**: ✅ Miễn phí - lấy danh sách giọng nói
   - **Text to Speech**: ⚠️ Tốn phí - tạo audio từ text
   - **Video Info**: Thông tin về video API

5. **Nhấn "Test API"** và xem kết quả

#### Demo Nhanh (Không Cần Host):

Bạn có thể mở file `test_ipad.html` trực tiếp từ Files app trên iPad:

```
Files → Browse → Tải file test_ipad.html về → Nhấn vào file → Mở bằng Safari
```

---

### 2. Test Python Script (Dùng Trên Mac/PC)

**File:** `test_api.py`

#### Yêu Cầu:
- Python 3.7+
- Thư viện `requests`

#### Cài Đặt:

```bash
# Clone repo
git clone https://github.com/MiniMax-AI/MiniMax-MCP.git
cd MiniMax-MCP

# Cài đặt dependencies
pip install requests
```

#### Sử dụng:

**Test cơ bản (chỉ test miễn phí):**
```bash
python test_api.py \
  --api-key YOUR_API_KEY_HERE \
  --api-host https://api.minimax.io
```

**Test đầy đủ (bao gồm test tốn phí):**
```bash
python test_api.py \
  --api-key YOUR_API_KEY_HERE \
  --api-host https://api.minimax.io \
  --include-paid
```

**Với văn bản tùy chỉnh:**
```bash
python test_api.py \
  --api-key YOUR_API_KEY_HERE \
  --api-host https://api.minimax.io \
  --include-paid \
  --text "Xin chào từ MiniMax!"
```

#### Kết Quả Mẫu:

```
🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪
     MINIMAX API TESTER
🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪

🔑 API Key: eyJhbGciOiJSUzI1NiI...
🌍 API Host: https://api.minimax.io

============================================================
🎤 Test 1: List Voices (Miễn phí)
============================================================
📡 Gọi API: https://api.minimax.io/v1/t2a/v2/list_voices
📊 Status Code: 200
✅ THÀNH CÔNG!

📋 Số lượng giọng nói: 150

🎵 Một số giọng nói có sẵn:
  - male-qn-qingse (青涩青年音色)
  - audiobook_female_1 (Female Audiobook)
  - cute_boy (Cute Boy)
  - Charming_Lady (Charming Lady)
  - presenter_male (Male Presenter)

============================================================
📊 TỔNG KẾT
============================================================

✅ Thành công: 1/1

🎉 API Key và Host của bạn hoạt động tốt!
   Bạn có thể sử dụng MiniMax MCP với các thông tin này.
```

---

## 🔑 Lấy API Key

### Khu Vực Global (Quốc Tế):
1. Truy cập: https://www.minimax.io/platform/user-center/basic-information/interface-key
2. Đăng nhập hoặc đăng ký tài khoản
3. Copy API Key
4. Sử dụng với Host: `https://api.minimax.io`

### Khu Vực China (Trung Quốc):
1. Truy cập: https://platform.minimaxi.com/user-center/basic-information/interface-key
2. Đăng nhập hoặc đăng ký tài khoản
3. Copy API Key
4. Sử dụng với Host: `https://api.minimaxi.com`

⚠️ **Quan trọng:** API Key và Host phải cùng khu vực, nếu không sẽ gặp lỗi "Invalid API Key"!

---

## 🐛 Xử Lý Lỗi Thường Gặp

### 1. Lỗi: "Invalid API key" hoặc 401 Unauthorized

**Nguyên nhân:**
- API Key không đúng
- API Key và Host không cùng khu vực

**Giải pháp:**
```
✅ Kiểm tra lại API Key có đúng không
✅ Đảm bảo API Key và Host khớp nhau:
   Global Key → Global Host (api.minimax.io)
   China Key  → China Host (api.minimaxi.com)
```

### 2. Lỗi: "Connection Error" hoặc "Timeout"

**Nguyên nhân:**
- Không có kết nối internet
- API Host không đúng
- Firewall/VPN chặn kết nối

**Giải pháp:**
```
✅ Kiểm tra kết nối internet
✅ Thử đổi sang khu vực khác (Global ↔ China)
✅ Tắt VPN nếu đang bật
✅ Thử lại sau vài phút
```

### 3. Lỗi: "CORS Error" (Trên Browser)

**Nguyên nhân:**
- Browser chặn request cross-origin

**Giải pháp:**
```
✅ Sử dụng extension "Allow CORS" trên Safari/Chrome
✅ Hoặc sử dụng Python script thay vì HTML
✅ Hoặc host file HTML trên cùng domain với API
```

### 4. Test Thành Công Nhưng Không Nghe Được Audio

**Nguyên nhân:**
- iPad không hỗ trợ format audio
- URL audio hết hạn

**Giải pháp:**
```
✅ Copy URL audio và mở trong tab mới
✅ Tải file về và mở bằng app Music
✅ Thử lại với format khác (mp3, flac, pcm)
```

---

## 📋 Checklist Kiểm Tra

Trước khi báo lỗi, hãy kiểm tra:

- [ ] API Key đã được copy đầy đủ (không thiếu ký tự)
- [ ] API Host đã chọn đúng khu vực
- [ ] Đã thử cả 2 công cụ test (HTML và Python)
- [ ] Internet đang hoạt động bình thường
- [ ] Đã đọc hướng dẫn xử lý lỗi ở trên

---

## ❓ FAQ

### Q1: Tôi có thể dùng MCP trên iPad không?

**A:** Không, MCP hiện tại không hỗ trợ iPad. Các công cụ test này chỉ giúp bạn kiểm tra **API** của MiniMax, không phải MCP server.

### Q2: Test thành công có nghĩa là MCP đã hoạt động trên iPad?

**A:** Không. Test thành công chỉ nghĩa là:
- ✅ API Key của bạn đúng
- ✅ Bạn có thể gọi API MiniMax thành công
- ❌ Nhưng MCP vẫn chưa hoạt động trên iPad

Để dùng MCP, bạn cần **Claude Desktop trên Mac/Windows**.

### Q3: Vậy các công cụ test này để làm gì?

**A:** Giúp bạn:
1. Kiểm tra API Key trước khi cấu hình MCP trên máy tính
2. Test API trực tiếp mà không cần MCP
3. Hiểu cách API hoạt động
4. Debug khi gặp vấn đề với MCP

### Q4: Tôi có thể tích hợp API vào app iOS của mình không?

**A:** Có! Bạn có thể:
- Sử dụng API REST của MiniMax trong Swift/Objective-C
- Tham khảo code trong `test_ipad.html` và `test_api.py`
- Đọc [API Documentation](https://www.minimax.io/docs) để biết thêm

### Q5: Test nào tốn phí, test nào miễn phí?

**A:**
- ✅ **Miễn phí:** List Voices, Query Video Status
- ⚠️ **Tốn phí:** Text to Speech, Voice Clone, Video Generation, Image Generation, Music Generation

Các test tốn phí được đánh dấu rõ ràng trong cả 2 công cụ.

---

## 🎓 Hướng Dẫn Sử Dụng MCP (Trên Desktop)

Nếu bạn muốn dùng MCP đầy đủ, hãy xem file [`HUONG_DAN_IPAD.md`](HUONG_DAN_IPAD.md) để biết:
- Cách cài đặt MCP trên Claude Desktop
- Cấu hình cho Cursor, Windsurf
- Các phương án thay thế cho iPad

---

## 🆘 Hỗ Trợ

Nếu vẫn gặp vấn đề:

1. **Kiểm tra Issues:** https://github.com/MiniMax-AI/MiniMax-MCP/issues
2. **Tạo Issue Mới:** Nếu chưa có ai gặp vấn đề tương tự
3. **Discord/Community:** Tham gia cộng đồng MiniMax

**Khi báo lỗi, hãy cung cấp:**
- Khu vực đang dùng (Global/China)
- Công cụ test đang dùng (HTML/Python)
- Error message đầy đủ
- Screenshot nếu có thể

---

## 📝 Tóm Tắt

| Điều | Trạng Thái |
|------|-----------|
| MCP hoạt động trên iPad | ❌ Không |
| Test API từ iPad | ✅ Có (qua HTML tool) |
| Test API từ Mac/PC | ✅ Có (qua Python script) |
| Sử dụng API trong app riêng | ✅ Có (REST API) |
| MCP hoạt động trên Claude Desktop | ✅ Có |

**Kết luận:**
- Nếu bạn muốn dùng MCP → Cần Claude Desktop trên Mac/Windows
- Nếu bạn chỉ cần test API → Dùng công cụ test trong repo này
- Nếu bạn muốn tích hợp vào app → Dùng REST API trực tiếp

---

## 🔗 Liên Kết Hữu Ích

- [MiniMax Platform (Global)](https://www.minimax.io)
- [MiniMax Platform (China)](https://platform.minimaxi.com)
- [API Documentation](https://www.minimax.io/docs)
- [MiniMax MCP GitHub](https://github.com/MiniMax-AI/MiniMax-MCP)
- [Claude Desktop](https://claude.ai/download)

---

**Chúc bạn test thành công! 🎉**
