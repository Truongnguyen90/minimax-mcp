# Hướng Dẫn Cài Đặt MiniMax MCP cho Claude trên iPad

## Giới Thiệu

MiniMax MCP Server cho phép bạn sử dụng các công cụ AI mạnh mẽ của MiniMax trên Claude, bao gồm:
- Chuyển văn bản thành giọng nói (Text to Speech)
- Nhân bản giọng nói (Voice Clone)
- Tạo video từ mô tả
- Tạo hình ảnh từ mô tả
- Tạo nhạc từ lời và giai điệu
- Thiết kế giọng nói tùy chỉnh

## Yêu Cầu Hệ Thống

**Lưu ý quan trọng:** Hiện tại, MCP (Model Context Protocol) chỉ hỗ trợ chính thức trên các ứng dụng desktop như:
- Claude Desktop (macOS/Windows)
- Cursor
- Windsurf
- OpenAI Agents

**Đối với iPad:** Claude trên iPad (app di động hoặc web) hiện chưa hỗ trợ trực tiếp MCP servers. Tuy nhiên, bạn có các lựa chọn sau:

## Các Phương Án Sử Dụng

### Phương Án 1: Sử dụng Claude Desktop trên Mac/PC (Khuyến Nghị)

Nếu bạn có máy Mac hoặc PC, đây là cách tốt nhất để sử dụng MiniMax MCP:

1. **Lấy API Key:**
   - Truy cập [MiniMax Global](https://www.minimax.io/platform/user-center/basic-information/interface-key) (Quốc tế)
   - Hoặc [MiniMax](https://platform.minimaxi.com/user-center/basic-information/interface-key) (Trung Quốc)
   - Sao chép API key của bạn

2. **Cài đặt UV (Python package manager):**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Cấu hình Claude Desktop:**
   - Mở Claude Desktop
   - Vào `Claude > Settings > Developer > Edit Config`
   - Dán nội dung sau vào file `claude_desktop_config.json`:

   ```json
   {
     "mcpServers": {
       "MiniMax": {
         "command": "uvx",
         "args": [
           "minimax-mcp",
           "-y"
         ],
         "env": {
           "MINIMAX_API_KEY": "DÁN_API_KEY_CỦA_BẠN_VÀO_ĐÂY",
           "MINIMAX_MCP_BASE_PATH": "/Users/TÊN_NGƯỜI_DÙNG/Desktop",
           "MINIMAX_API_HOST": "https://api.minimax.io",
           "MINIMAX_API_RESOURCE_MODE": "url"
         }
       }
     }
   }
   ```

4. **Lưu ý quan trọng về API Host:**
   - **Quốc tế:** Sử dụng `https://api.minimax.io`
   - **Trung Quốc:** Sử dụng `https://api.minimaxi.com`
   - API Key và Host phải cùng khu vực, nếu không sẽ báo lỗi "Invalid API key"

5. **Khởi động lại Claude Desktop** để áp dụng cấu hình

### Phương Án 2: Sử dụng qua Web API (Cho iPad)

Nếu bạn chỉ có iPad, bạn có thể:

1. **Sử dụng trực tiếp API của MiniMax:**
   - Truy cập [MiniMax Platform](https://www.minimax.io/platform)
   - Sử dụng API documentation để gọi trực tiếp các API
   - Tích hợp vào ứng dụng của riêng bạn

2. **Sử dụng Remote MCP Server:**
   - Deploy MCP server lên cloud (VPS, cloud server)
   - Sử dụng transport mode SSE thay vì stdio
   - Kết nối từ xa từ iPad (yêu cầu cấu hình nâng cao)

### Phương Án 3: Chờ Hỗ Trợ MCP trên Mobile

Anthropic có thể sẽ hỗ trợ MCP trên các ứng dụng mobile trong tương lai. Hãy theo dõi:
- [Claude Updates](https://www.anthropic.com/news)
- [MiniMax GitHub](https://github.com/MiniMax-AI/MiniMax-MCP)

## Cấu Hình Chi Tiết

### Các Biến Môi Trường

| Biến | Mô Tả | Bắt Buộc |
|------|-------|----------|
| `MINIMAX_API_KEY` | API key từ MiniMax platform | Có |
| `MINIMAX_MCP_BASE_PATH` | Thư mục lưu file đầu ra (video, audio, ảnh) | Có |
| `MINIMAX_API_HOST` | URL của API server | Có |
| `MINIMAX_API_RESOURCE_MODE` | Cách trả về tài nguyên: `url` hoặc `local` | Không (mặc định: url) |

### Chọn API Host Đúng

**Quan trọng:** API Key và Host phải cùng khu vực!

| Khu Vực | API Key | API Host |
|---------|---------|----------|
| **Quốc Tế** | [Lấy tại đây](https://www.minimax.io/platform/user-center/basic-information/interface-key) | `https://api.minimax.io` |
| **Trung Quốc** | [Lấy tại đây](https://platform.minimaxi.com/user-center/basic-information/interface-key) | `https://api.minimaxi.com` |

## Các Công Cụ Có Sẵn

Sau khi cài đặt thành công, bạn sẽ có các công cụ sau trong Claude:

| Công Cụ | Mô Tả |
|---------|-------|
| `text_to_audio` | Chuyển văn bản thành giọng nói |
| `list_voices` | Liệt kê tất cả giọng nói có sẵn |
| `voice_clone` | Nhân bản giọng nói từ file audio |
| `generate_video` | Tạo video từ mô tả văn bản |
| `text_to_image` | Tạo hình ảnh từ mô tả văn bản |
| `music_generation` | Tạo nhạc từ mô tả và lời bài hát |
| `voice_design` | Thiết kế giọng nói tùy chỉnh |
| `query_video_generation` | Kiểm tra trạng thái tạo video |

## Ví Dụ Sử Dụng

Sau khi cài đặt, bạn có thể yêu cầu Claude:

- "Hãy tạo một đoạn audio đọc văn bản này bằng giọng nữ"
- "Tạo video về một con mèo đang chơi đùa trong vườn"
- "Tạo hình ảnh phong cảnh núi non hùng vĩ lúc hoàng hôn"
- "Tạo một bản nhạc vui tươi với lời ca về mùa hè"

## Xử Lý Lỗi Thường Gặp

### Lỗi: "Invalid API key"
**Nguyên nhân:** API Key và Host không cùng khu vực

**Giải pháp:**
- Kiểm tra lại bạn đang dùng API Key từ khu vực nào
- Đảm bảo `MINIMAX_API_HOST` khớp với khu vực của API Key

### Lỗi: "spawn uvx ENOENT"
**Nguyên nhân:** Hệ thống không tìm thấy lệnh `uvx`

**Giải pháp:**
1. Kiểm tra đường dẫn uvx:
   ```bash
   which uvx
   ```
2. Sử dụng đường dẫn đầy đủ trong config (ví dụ: `/usr/local/bin/uvx`)

## Hỗ Trợ

- **Tài liệu:** [README](README.md) | [中文文档](README-CN.md)
- **GitHub Issues:** [MiniMax-MCP Issues](https://github.com/MiniMax-AI/MiniMax-MCP/issues)
- **MiniMax Platform:** [https://www.minimax.io](https://www.minimax.io)

## Lưu Ý Về Chi Phí

⚠️ **Cảnh báo:** Sử dụng các công cụ MiniMax sẽ tốn phí theo giá của MiniMax Platform. Hãy kiểm tra bảng giá tại [MiniMax Pricing](https://www.minimax.io/platform) trước khi sử dụng.

## Kết Luận

Mặc dù MCP chưa hỗ trợ trực tiếp trên iPad, bạn vẫn có thể:
1. Sử dụng Claude Desktop trên Mac/PC để trải nghiệm đầy đủ tính năng MCP
2. Sử dụng trực tiếp API của MiniMax qua các công cụ khác
3. Chờ đợi hỗ trợ MCP trên mobile trong tương lai

Nếu bạn có câu hỏi hoặc gặp vấn đề, vui lòng tạo issue tại [GitHub repository](https://github.com/MiniMax-AI/MiniMax-MCP/issues).
