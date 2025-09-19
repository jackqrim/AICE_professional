#!/usr/bin/env python3
"""
AICE Professional Course - Dependency Test Script
테스트 스크립트: 필요한 패키지들이 올바르게 설치되었는지 확인합니다.
"""

import sys

def test_imports():
    """필수 패키지들의 import를 테스트합니다."""
    
    packages = [
        ('numpy', 'numpy'),
        ('pandas', 'pandas'),
        ('matplotlib', 'matplotlib.pyplot'),
        ('sklearn', 'scikit-learn'),
        ('bs4', 'beautifulsoup4'),
        ('nltk', 'nltk'),
        ('tensorflow', 'tensorflow'),
        ('gensim', 'gensim'),
    ]
    
    results = []
    
    print("=" * 50)
    print("AICE Professional Course - 패키지 설치 확인")
    print("=" * 50)
    
    for module_name, package_name in packages:
        try:
            __import__(module_name)
            print(f"✅ {package_name}: 설치됨")
            results.append((package_name, True, None))
        except ImportError as e:
            print(f"❌ {package_name}: 설치되지 않음")
            print(f"   설치 명령: pip install {package_name}")
            results.append((package_name, False, str(e)))
    
    print("\n" + "=" * 50)
    
    # BeautifulSoup 특별 테스트
    try:
        from bs4 import BeautifulSoup
        import bs4
        
        # 기본 기능 테스트
        html = "<html><body><h1>Test</h1></body></html>"
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('h1').text
        
        print(f"🎉 BeautifulSoup 기능 테스트 성공!")
        print(f"   버전: {bs4.__version__}")
        print(f"   테스트 결과: {title}")
        
    except Exception as e:
        print(f"⚠️  BeautifulSoup 기능 테스트 실패: {e}")
    
    print("=" * 50)
    
    # 결과 요약
    success_count = sum(1 for _, success, _ in results if success)
    total_count = len(results)
    
    print(f"설치 완료: {success_count}/{total_count} 패키지")
    
    if success_count == total_count:
        print("🎉 모든 필수 패키지가 성공적으로 설치되었습니다!")
        return True
    else:
        print("⚠️  일부 패키지가 설치되지 않았습니다.")
        print("   requirements.txt를 사용하여 모든 패키지를 설치하세요:")
        print("   pip install -r requirements.txt")
        return False

if __name__ == "__main__":
    success = test_imports()
    sys.exit(0 if success else 1)