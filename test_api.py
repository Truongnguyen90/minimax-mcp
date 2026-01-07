#!/usr/bin/env python3
"""
Script kiểm tra MiniMax API
Test các API endpoints của MiniMax để đảm bảo API key và host hoạt động đúng.

Sử dụng:
    python test_api.py --api-key YOUR_API_KEY --api-host https://api.minimax.io
"""

import argparse
import requests
import json
import sys
from typing import Dict, Any


class MiniMaxAPITester:
    """Test MiniMax API endpoints"""

    def __init__(self, api_key: str, api_host: str):
        self.api_key = api_key
        self.api_host = api_host.rstrip('/')
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

    def test_list_voices(self) -> Dict[str, Any]:
        """
        Test list voices API endpoint.
        Endpoint này miễn phí, chỉ lấy danh sách giọng nói có sẵn.
        """
        print("\n" + "=" * 60)
        print("🎤 Test 1: List Voices (Miễn phí)")
        print("=" * 60)

        url = f"{self.api_host}/v1/t2a/v2/list_voices"

        try:
            print(f"📡 Gọi API: {url}")
            response = requests.get(url, headers=self.headers, timeout=10)

            print(f"📊 Status Code: {response.status_code}")

            if response.status_code == 200:
                data = response.json()
                print("✅ THÀNH CÔNG!")
                print(f"\n📋 Số lượng giọng nói: {len(data.get('data', {}).get('voices', []))}")

                # Hiển thị 5 giọng đầu tiên
                voices = data.get('data', {}).get('voices', [])[:5]
                if voices:
                    print("\n🎵 Một số giọng nói có sẵn:")
                    for voice in voices:
                        print(f"  - {voice.get('voice_id')} ({voice.get('name', 'N/A')})")

                return {"success": True, "data": data}
            else:
                error_data = response.json()
                print("❌ LỖI!")
                print(f"\n📄 Chi tiết lỗi:")
                print(json.dumps(error_data, indent=2, ensure_ascii=False))
                return {"success": False, "error": error_data}

        except requests.exceptions.Timeout:
            print("❌ LỖI: Timeout - API không phản hồi trong thời gian cho phép")
            return {"success": False, "error": "Timeout"}
        except requests.exceptions.ConnectionError:
            print("❌ LỖI: Không thể kết nối đến API server")
            print(f"   Kiểm tra lại API Host: {self.api_host}")
            return {"success": False, "error": "Connection Error"}
        except Exception as e:
            print(f"❌ LỖI: {str(e)}")
            return {"success": False, "error": str(e)}

    def test_text_to_speech(self, text: str = "Xin chào, đây là test!") -> Dict[str, Any]:
        """
        Test text to speech API endpoint.
        ⚠️ Endpoint này TỐN PHÍ - chỉ test khi cần thiết!
        """
        print("\n" + "=" * 60)
        print("🔊 Test 2: Text to Speech (⚠️ TỐN PHÍ)")
        print("=" * 60)

        url = f"{self.api_host}/v1/t2a/v2"

        payload = {
            "model": "speech-01-turbo",
            "text": text,
            "voice_setting": {
                "voice_id": "male-qn-qingse",
                "speed": 1.0,
                "vol": 1.0,
                "pitch": 0
            },
            "audio_setting": {
                "sample_rate": 32000,
                "bitrate": 128000,
                "format": "mp3"
            }
        }

        try:
            print(f"📡 Gọi API: {url}")
            print(f"📝 Văn bản: {text}")
            print(f"⚠️  CẢNH BÁO: API call này sẽ tốn phí!")

            confirm = input("\n❓ Bạn có muốn tiếp tục? (yes/no): ")
            if confirm.lower() not in ['yes', 'y']:
                print("🚫 Đã hủy test Text to Speech")
                return {"success": False, "error": "User cancelled"}

            response = requests.post(
                url,
                headers=self.headers,
                json=payload,
                timeout=30
            )

            print(f"📊 Status Code: {response.status_code}")

            if response.status_code == 200:
                data = response.json()
                print("✅ THÀNH CÔNG!")

                audio_url = data.get('data', {}).get('audio_file') or data.get('audio_file')
                if audio_url:
                    print(f"\n🎵 URL Audio: {audio_url}")
                    print("   (Mở URL này trong browser để nghe)")

                return {"success": True, "data": data}
            else:
                error_data = response.json()
                print("❌ LỖI!")
                print(f"\n📄 Chi tiết lỗi:")
                print(json.dumps(error_data, indent=2, ensure_ascii=False))
                return {"success": False, "error": error_data}

        except Exception as e:
            print(f"❌ LỖI: {str(e)}")
            return {"success": False, "error": str(e)}

    def run_all_tests(self, skip_paid: bool = True):
        """Chạy tất cả các test"""
        print("\n" + "🧪" * 30)
        print("     MINIMAX API TESTER")
        print("🧪" * 30)
        print(f"\n🔑 API Key: {self.api_key[:20]}...")
        print(f"🌍 API Host: {self.api_host}")

        results = {}

        # Test 1: List voices (miễn phí)
        results['list_voices'] = self.test_list_voices()

        # Test 2: Text to Speech (tốn phí)
        if not skip_paid:
            results['text_to_speech'] = self.test_text_to_speech()
        else:
            print("\n" + "=" * 60)
            print("⏭️  Bỏ qua các test tốn phí (sử dụng --include-paid để test)")
            print("=" * 60)

        # Tổng kết
        print("\n" + "=" * 60)
        print("📊 TỔNG KẾT")
        print("=" * 60)

        success_count = sum(1 for r in results.values() if r.get('success'))
        total_count = len(results)

        print(f"\n✅ Thành công: {success_count}/{total_count}")

        if results.get('list_voices', {}).get('success'):
            print("\n🎉 API Key và Host của bạn hoạt động tốt!")
            print("   Bạn có thể sử dụng MiniMax MCP với các thông tin này.")
        else:
            print("\n⚠️  Có vấn đề với API Key hoặc Host:")
            print("   1. Kiểm tra API Key có đúng không")
            print("   2. Đảm bảo API Key và Host cùng khu vực:")
            print("      - Global: https://api.minimax.io")
            print("      - China: https://api.minimaxi.com")

        return results


def main():
    parser = argparse.ArgumentParser(
        description='Test MiniMax API endpoints',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ví dụ sử dụng:
  # Test với API Key và Host (chỉ test miễn phí)
  python test_api.py --api-key YOUR_KEY --api-host https://api.minimax.io

  # Test tất cả (bao gồm cả test tốn phí)
  python test_api.py --api-key YOUR_KEY --api-host https://api.minimax.io --include-paid

Lấy API Key:
  - Global: https://www.minimax.io/platform/user-center/basic-information/interface-key
  - China: https://platform.minimaxi.com/user-center/basic-information/interface-key

Chú ý:
  - API Key và Host phải cùng khu vực (Global hoặc China)
  - Một số test sẽ tốn phí, được đánh dấu rõ ràng
        """
    )

    parser.add_argument(
        '--api-key',
        required=True,
        help='MiniMax API Key'
    )

    parser.add_argument(
        '--api-host',
        required=True,
        choices=['https://api.minimax.io', 'https://api.minimaxi.com'],
        help='MiniMax API Host (phải khớp với khu vực của API Key)'
    )

    parser.add_argument(
        '--include-paid',
        action='store_true',
        help='Bao gồm các test tốn phí (mặc định: chỉ test miễn phí)'
    )

    parser.add_argument(
        '--text',
        default='Xin chào, đây là test từ MiniMax API!',
        help='Văn bản để test Text to Speech (nếu --include-paid được bật)'
    )

    args = parser.parse_args()

    # Tạo tester và chạy
    tester = MiniMaxAPITester(args.api_key, args.api_host)
    results = tester.run_all_tests(skip_paid=not args.include_paid)

    # Exit code dựa trên kết quả
    if results.get('list_voices', {}).get('success'):
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
