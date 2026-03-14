import json

company_list_raw = """한국전자통신연구원
한국화학연구원
한국에너지기술연구원
한국지질자원연구원
한국생명공학연구원
한국원자력연구원
한국표준과학연구원
한국기계연구원
한국기초과학지원연구원 부설 국가핵융합연구소
한국기초과학지원연구원
한국항공우주연구원
한국과학기술정보연구원
한국화학연구원 부설 안전성평가연구소
한국해양과학기술원 부설 선박해양플랜트 연구소
한국한의학연구원
한국천문연구원
한국전자통신연구원 부설 국가보안기술연구소
기초과학연구원 부설 국가수리과학연구소
기초과학연구원
한국과학기술원 부설 나노종합기술원
한국연구재단
한국원자력안전기술원
정보통신산업진흥원 부설 정보통신기술진흥센터
한국원자력통제기술원
한국산업기술시험원 중부지역본부
국방과학연구소
배재대학교
과학기술연합대학원대학교(UST)
충남대학교
한국과학기술원
대덕대학교
한남대학교
한밭대학교
(재)다차원스마트 IT융합시스템연구단
대전교육과학연구원
한국전력공사 전력연구원
K-water 연구원
교통안전공단 중부지역본부
안전보건공단 산업안전보건연구원 산업화학연구실(화학물질독성연구실)
한국건설생활환경시험연구원 대전충남지원
한국토지주택공사 토지주택연구원
한국수력원자력㈜ 중앙연구원
국제지식재산연수원
금강유역환경청
국립중앙과학관
대전인재개발원
대전교육정보원
대전지방기상청
대전충남지방중소기업청
대전세관
정부통합전산센터
화학물질안전원
대전광역시 시설관리공단 무지개복지센터
한국전력기술㈜ 원자로설계개발단
연구개발특구진흥재단
(재)대전경제통상진흥원
대전직업능력개발원
한국원자력연료㈜
안전보건공단 대전지역본부
(재)대전테크노파크
한국조폐공사
한국원자력환경공단
대전시민천문대
중소기업기술정보진흥원
대전충남KOTRA지원단
대전신용보증재단 북부지점
중소기업진흥공단 청년사관학교
국가과학기술인력개발원 교육센터
창업진흥원
한국서부발전
대전창조경제혁신센터
한국수자원공사
정보통신기획평가원
한국철도공사
코레일테크㈜
한국철도시설공단
한국산림복지진흥원
한국가스기술공사
소상공인진흥공단
신용보증재단중앙회
목원대학교 산학협력단
(사)한국방사성폐기물학회
대덕이노폴리스 벤처협회
대전대학교 산학협력단
대덕산업단지관리공단
한국여성원자력전문인협회
대한산업보건협회 대전산업보건센터
(사)출연(연)연구발전협의회 총연합회
대한산업안전협회 대전지역본부
(사)대덕클럽
한국단미사료협회
(재)한국원자력협력재단
(재)장애인기업종합지원센터
대덕연구개발특구기관장협의회
(재)중앙문화재연구원 대전사무소
대전지역사업평가단
대전녹색환경지원센터
(사)대한여성과학기술인회
한국표준협회 대전세종충남지역본부
창업진흥원 창업보육센터
대덕원자력포럼
한국산업기술진흥협회
한국기술사업화진흥협회
한국여성경제인협회
대전문화산업진흥협회
한국과학기술단체총연합회 (과총)
(재)기가코리아사업단
나노융합산업연구조합
바이오메스연구단
(사)과학기술연우연합회
계룡건설산업
골프존
나노신소재
나노팀
나노엔텍
네오팜
노타
뉴로스
대산F&B
동양에스텍
디엔에프
라이온켐텍
라이트론
레인보우로보틱스
리가켐바이오
리메드
민테크
바이오니아
비비씨
비플라이소프트
빛과전자
수젠텍
시스웍
신테카바이오
쎄트렉아이
아이디스
아이디스홀딩스
아이비전웍스
아이쓰리시스템
아이빔테크놀로지
안지오랩
알루코
알테오젠
에르코스
에이치엔에스하이텍
엔지켐생명과학
오름테라퓨틱
와이바이오로직스
우성
원텍
위드텍
위월드
이비테크
인텍플러스
인투셀
잼코
제노텍
제일사료
젬백스
지노믹트리
진시스템
컨텍
크로우
큐로셀
토모큐브
파이버프로
펩트론
플라즈맵
프리시젼바이오
한독크린텍
한빛레이저
한온시스템
한켐
HLB제넥스
HLB파나진
KT&G
KTcs
LX세미콘"""
all_companies = [c.strip() for c in company_list_raw.splitlines() if c.strip()]

parsed_data = [
    ('3/23', '공공', '조연우', '대전광역시 외국인주민 통합지원센터'),
    ('3/23', '상장', '조연우', '월드번역원((주)월시스)'),
    ('3/23', '공공', '허준혁', '정부통합전산센터'),
    ('3/23', '공공', '오채영', '소상공인진흥공단'),
    ('3/23', '상장', '오채영', '한독크린텍'),
    ('3/30', '공공', '구현경', '대전녹색환경지원센터'),
    ('3/30', '공공', '원창호', '한국항공우주연구원'),
    ('3/30', '공공', '백재현', '대전지방기상청'),
    ('3/30', '상장', '허준혁', '비플라이소프트'),
    ('3/30', '공공', '이승주', '한국수자원공사'),
    ('3/30', '상장', '강체첵', 'KT&G'),
    ('3/30', '상장', '진승훈', '큐로셀'),
    ('3/23', '상장', '전은재', '쎄트렉아이'),
    ('4/6', '상장', '구현경', 'KT&G'),
    ('4/6', '공공', '오다인', '대전직업능력개발원'),
    ('4/6', '공공', '박해원', '정보통신기획평가원'),
    ('4/6', '상장', '이승주', '계룡건설산업'),
    ('4/6', '상장', '백재현', '에르코스'),
    ('4/6', '공공', '이현기', '한국철도시설공단'),
    ('4/13', '공공', '양하영', '국방과학연구소'),
    ('4/13', '공공', '이수호', '한국전자통신연구원'),
    ('4/13', '상장', '정현준', '동양에스텍'),
    ('4/13', '상장', '원창호', '펩트론'),
    ('4/13', '상장', '안은률', '대산F&B'),
    ('4/13', '공공', '이준성', '중소기업기술정보진흥원'),
    ('4/6', '공공', '유태수', '코레일테크㈜'),
    ('4/13', '상장', '곽현지', '골프존'),
    ('4/20', '공공', '구민경', '대전시민천문대'),
    ('4/20', '공공', '신재민', '한국가스기술공사'),
    ('4/20', '공공', '진승훈', '신용보증재단중앙회'),
    ('5/4', '공공', '김채은', '대전세관'),
    ('5/4', '상장', '오다인', '우성'),
    ('5/4', '상장', '이수호', '인텍플러스'),
    ('5/4', '상장', '박해원', '아이디스'),
    ('5/4', '상장', '이준희', 'KTcs'),
    ('5/4', '상장', '정구영', '코셈'),
    ('5/11', '공공', '안은률', '대전문화산업진흥협회'),
    ('5/11', '상장', '김주헌', '아이디스홀딩스'),
    ('5/11', '공공', '김주헌', '안전보건공단대전지역본부'),
    ('5/11', '상장', '이준성', '위드텍'),
    ('5/11', '상장', '유태수', '지노믹트리'),
    ('5/11', '공공', '한성경', '한국산림복지진흥원'),
    ('5/11', '공공', '이채원', '대전창조경제혁신센터'),
    ('5/18', '상장', '양하영', '알루코'),
    ('5/18', '공공', '정현준', '한국화학연구원'),
    ('5/18', '상장', '정하진', '원텍'),
    ('5/18', '공공', '정구영', '한국수자원공사'),
    ('5/18', '상장', '이채원', '네오팜'),
    ('5/18', '공공', '전은재', '한국기계연구원'),
    ('5/18', '공공', '곽현지', '(재)대전경제통상진흥원'),
    ('6/1', '상장', '구민경', '컨텍'),
    ('6/1', '공공', '양예지', '대전도시공사'),
    ('6/1', '상장', '신재민', '파이버프로'),
    ('6/1', '상장', '양예지', '레인보우로보틱스')
]
dates = ['3/23', '3/30', '4/6', '4/13', '4/20', '5/4', '5/11', '5/18', '6/1']

# Tracking duplicates
from collections import defaultdict
company_count = defaultdict(list)
for item in parsed_data:
    pd, pg, pn, pc = item
    norm_c = str(pc).lower().replace(" ", "")
    if norm_c == "k-water": norm_c = "한국수자원공사"
    elif "코레일테크" in norm_c: norm_c = "코레일테크㈜"
    elif "경제통상" in norm_c: norm_c = "(재)대전경제통상진흥원"
    elif norm_c == "kt&g": norm_c = "KT&G"
    elif norm_c == "대산f&b": norm_c = "대산F&B"
    company_count[norm_c].append(item)

duplicates_norm = {k: v for k, v in company_count.items() if len(v) > 1}

# Organize data per date
schedule_obj = []
for d in dates:
    pubs = []
    pris = []
    
    for pd, pg, pn, pc in parsed_data:
        if pd == d:
            norm_c = str(pc).lower().replace(" ", "")
            if norm_c == "k-water": norm_c = "한국수자원공사"
            elif "코레일테크" in norm_c: norm_c = "코레일테크㈜"
            elif "경제통상" in norm_c: norm_c = "(재)대전경제통상진흥원"
            elif norm_c == "kt&g": norm_c = "KT&G"
            elif norm_c == "대산f&b": norm_c = "대산F&B"
            
            error_msg = ""
            if pn == '유태수' and pd == '4/6':
                error_msg = "6주차(4/13) 게시판에 등록했으나 4/6으로 기재함"
                
            if norm_c in duplicates_norm:
                others = [f"{o_pn}({o_pd})" for o_pd, o_pg, o_pn, o_pc in duplicates_norm[norm_c] if o_pn != pn or o_pd != pd]
                if others:
                    if error_msg: error_msg += " | "
                    error_msg += f"중복선정: {', '.join(others)}와 동일"
            
            entry = {"name": pn, "company": pc, "error": error_msg}
            if pg == '공공':
                pubs.append(entry)
            else:
                pris.append(entry)
                
    while len(pubs) < 4: pubs.append({"name": "", "company": "", "error": ""})
    while len(pris) < 4: pris.append({"name": "", "company": "", "error": ""})
    
    schedule_obj.append({"date": d, "public": pubs[:4], "private": pris[:4]})

html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>지역사회의 이해 발표 일정</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Noto+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-color: #0f172a;
            --card-bg: rgba(255, 255, 255, 0.05);
            --card-border: rgba(255, 255, 255, 0.1);
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --accent: #3b82f6;
            --accent-glow: rgba(59, 130, 246, 0.5);
            --error: #ef4444;
            --success: #10b981;
            --pub-color: #8b5cf6;
            --pri-color: #f59e0b;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Inter', 'Noto Sans KR', sans-serif;
        }}

        body {{
            background-color: var(--bg-color);
            background-image: 
                radial-gradient(at 0% 0%, rgba(59, 130, 246, 0.15) 0px, transparent 50%),
                radial-gradient(at 100% 100%, rgba(139, 92, 246, 0.15) 0px, transparent 50%);
            background-attachment: fixed;
            color: var(--text-main);
            min-height: 100vh;
            padding: 2rem;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}

        header {{
            text-align: center;
            margin-bottom: 3rem;
            animation: fadeInDown 0.8s ease-out;
        }}

        h1 {{
            font-size: 2.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #60a5fa, #c084fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }}
        
        header p {{
            color: var(--text-muted);
            font-size: 1.1rem;
        }}

        .schedule-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
            gap: 2rem;
            width: 100%;
            max-width: 1400px;
        }}

        .date-card {{
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 20px;
            padding: 1.5rem;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            animation: fadeIn 0.8s ease-out backwards;
        }}

        .date-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.3);
            border-color: rgba(255, 255, 255, 0.2);
        }}

        .date-header {{
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid var(--card-border);
            text-align: center;
            color: #e2e8f0;
        }}

        .sections-container {{
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }}

        .section-title {{
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .title-pub {{ color: var(--pub-color); }}
        .title-pri {{ color: var(--pri-color); }}

        .slot {{
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
            margin-bottom: 1rem;
            background: rgba(0,0,0,0.2);
            padding: 12px;
            border-radius: 12px;
            border: 1px solid transparent;
            transition: border-color 0.2s;
        }}
        
        .slot:hover {{
            border-color: rgba(255,255,255,0.1);
        }}

        .inputs-row {{
            display: flex;
            gap: 1rem;
        }}

        select, input {{
            width: 100%;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--card-border);
            color: var(--text-main);
            padding: 0.75rem 1rem;
            border-radius: 8px;
            font-size: 0.95rem;
            outline: none;
            transition: all 0.2s ease;
        }}

        select {{
            flex: 2;
            cursor: pointer;
            appearance: none;
            background-image: url("data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%2394a3b8%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E");
            background-repeat: no-repeat;
            background-position: right 1rem top 50%;
            background-size: 0.65rem auto;
            padding-right: 2.5rem;
        }}

        select option {{
            background: var(--bg-color);
            color: var(--text-main);
        }}

        input {{
            flex: 1;
        }}

        select:focus, input:focus {{
            border-color: var(--accent);
            box-shadow: 0 0 0 2px var(--accent-glow);
            background: rgba(255, 255, 255, 0.1);
        }}

        .error-msg {{
            color: var(--error);
            font-size: 0.85rem;
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 4px;
            animation: pulse 2s infinite;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        @keyframes fadeInDown {{
            from {{ opacity: 0; transform: translateY(-20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        @keyframes pulse {{
            0% {{ opacity: 0.8; }}
            50% {{ opacity: 1; text-shadow: 0 0 8px rgba(239, 68, 68, 0.4); }}
            100% {{ opacity: 0.8; }}
        }}

        @media (max-width: 768px) {{
            .schedule-grid {{
                grid-template-columns: 1fr;
            }}
            .inputs-row {{
                flex-direction: column;
            }}
        }}
    </style>
</head>
<body>

    <header>
        <h1>발표 일정 관리 보드</h1>
        <p>각 날짜별 공공기관 및 상장기업 발표자를 관리하세요.</p>
    </header>

    <div class="schedule-grid" id="grid">
        <!-- Rendered via JS -->
    </div>

    <script>
        const companies = {json.dumps(all_companies, ensure_ascii=False)};
        const schedule = {json.dumps(schedule_obj, ensure_ascii=False)};

        function generateOptions(selectedValue) {{
            let options = '<option value="">-- 기업 선택 --</option>';
            // Add selected value if it's not in the list to preserve it
            let found = false;
            companies.forEach(company => {{
                const isSelected = company === selectedValue ? 'selected' : '';
                if(isSelected) found = true;
                options += `<option value="${{company}}" ${{isSelected}}>${{company}}</option>`;
            }});
            
            if (selectedValue && !found) {{
                options += `<option value="${{selectedValue}}" selected>${{selectedValue}} (목록 외)</option>`;
            }}
            return options;
        }}

        function createSlot(data, type) {{
            return `
                <div class="slot">
                    <div class="inputs-row">
                        <select>
                            ${{generateOptions(data.company)}}
                        </select>
                        <input type="text" placeholder="이름 입력" value="${{data.name}}">
                    </div>
                    ${{data.error ? `<div class="error-msg">⚠️ ${{data.error}}</div>` : ''}}
                </div>
            `;
        }}

        const grid = document.getElementById('grid');

        schedule.forEach((day, index) => {{
            const card = document.createElement('div');
            card.className = 'date-card';
            card.style.animationDelay = `${{index * 0.1}}s`;

            card.innerHTML = `
                <div class="date-header">🗓️ ${{day.date}}</div>
                <div class="sections-container">
                    <div class="section">
                        <div class="section-title title-pub">🏛️ 공공기관 (최대 4명)</div>
                        ${{day.public.map(slot => createSlot(slot, 'pub')).join('')}}
                    </div>
                    <div class="section">
                        <div class="section-title title-pri">🏢 상장기업 (최대 4명)</div>
                        ${{day.private.map(slot => createSlot(slot, 'pri')).join('')}}
                    </div>
                </div>
            `;
            grid.appendChild(card);
        }});
    </script>
</body>
</html>
"""

with open('c:/Users/Sumin/00_Projects/지역사회의이해발표시트/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
