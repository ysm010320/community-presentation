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
    ('3/23', '공공', '조연우', '대전광역시 외국인주민 통합지원센터', '3.8. 14:15'),
    ('3/23', '상장', '조연우', '월드번역원((주)월시스)', '3.8. 14:15'),
    ('3/23', '공공', '허준혁', '정부통합전산센터', '3.8. 14:02'),
    ('3/23', '공공', '오채영', '소상공인진흥공단', '3.8. 14:19'),
    ('3/23', '상장', '오채영', '한독크린텍', '3.8. 14:19'),
    ('3/30', '공공', '구현경', '대전녹색환경지원센터', '3.8. 14:38'),
    ('3/30', '공공', '원창호', '한국항공우주연구원', '3.10. 11:29'),
    ('3/30', '공공', '백재현', '대전지방기상청', '3.10. 12:57'),
    ('3/30', '상장', '허준혁', '비플라이소프트', '3.8. 14:02'),
    ('3/30', '공공', '이승주', '한국수자원공사', '3.10. 17:33'),
    ('3/30', '상장', '강체첵', 'KT&G', '3.13. 13:58'),
    ('3/30', '상장', '진승훈', '큐로셀', '3.14. 23:25'),
    ('3/23', '상장', '전은재', '쎄트렉아이', '3.15. 16:51'),
    ('4/6', '상장', '구현경', 'KT&G', '3.17. 15:43'),
    ('4/6', '공공', '오다인', '대전직업능력개발원', '3.20. 20:30'),
    ('4/6', '공공', '박해원', '정보통신기획평가원', '3.20. 20:31'),
    ('4/6', '상장', '이승주', '계룡건설산업', '3.20. 20:34'),
    ('4/6', '상장', '백재현', '에르코스', '3.21. 20:25'),
    ('4/6', '공공', '이현기', '한국철도시설공단', '3.21. 23:14'),
    ('4/13', '공공', '양하영', '국방과학연구소', '4.3. 11:13'),
    ('4/13', '공공', '이수호', '한국전자통신연구원', '4.3. 11:15'),
    ('4/13', '상장', '정현준', '동양에스텍', '4.3. 11:16'),
    ('4/13', '상장', '원창호', '펩트론', '4.3. 11:20'),
    ('4/13', '상장', '안은률', '대산F&B', '4.3. 11:21'),
    ('4/13', '공공', '이준성', '중소기업기술정보진흥원', '4.3. 11:58'),
    ('4/6', '공공', '유태수', '코레일테크㈜', '4.4. 11:39'),
    ('4/13', '상장', '곽현지', '골프존', '4.5. 17:01'),
    ('4/20', '공공', '구민경', '대전시민천문대', '4.13. 11:28'),
    ('4/20', '공공', '신재민', '한국가스기술공사', '4.13. 11:29'),
    ('4/20', '공공', '진승훈', '신용보증재단중앙회', '4.14. 02:26'),
    ('5/4', '공공', '김채은', '대전세관', '4.20. 23:44'),
    ('5/4', '상장', '오다인', '우성', '4.26. 17:54'),
    ('5/4', '상장', '이수호', '인텍플러스', '4.26. 17:55'),
    ('5/4', '상장', '박해원', '아이디스', '4.27. 12:35'),
    ('5/4', '상장', '이준희', 'KTcs', '4.28. 20:53'),
    ('5/4', '상장', '정구영', '코셈', '5.1. 11:27'),
    ('5/11', '공공', '안은률', '대전문화산업진흥협회', '5.3. 12:44'),
    ('5/11', '상장', '김주헌', '아이디스홀딩스', '5.3. 21:05'),
    ('5/11', '공공', '김주헌', '안전보건공단대전지역본부', '5.3. 21:05'),
    ('5/11', '상장', '이준성', '위드텍', '5.4. 11:59'),
    ('5/11', '상장', '유태수', '지노믹트리', '5.5. 15:46'),
    ('5/11', '공공', '한성경', '한국산림복지진흥원', '5.5. 23:25'),
    ('5/11', '공공', '이채원', '대전창조경제혁신센터', '5.5. 23:36'),
    ('5/18', '상장', '양하영', '알루코', '5.10. 12:41'),
    ('5/18', '공공', '정현준', '한국화학연구원', '5.10. 12:43'),
    ('5/18', '상장', '정하진', '원텍', '5.10. 21:30'),
    ('5/18', '공공', '정구영', '한국수자원공사', '5.11. 11:21'),
    ('5/18', '상장', '이채원', '네오팜', '5.12. 12:53'),
    ('5/18', '공공', '전은재', '한국기계연구원', '5.12. 12:56'),
    ('5/18', '공공', '곽현지', '(재)대전경제통상진흥원', '5.13. 12:56'),
    ('6/1', '상장', '구민경', '컨텍', '5.24. 13:51'),
    ('6/1', '공공', '양예지', '대전도시공사', '5.24. 13:52'),
    ('6/1', '상장', '신재민', '파이버프로', '5.24. 13:53'),
    ('6/1', '상장', '양예지', '레인보우로보틱스', '5.24. 13:54')
]
dates = ['3/23', '3/30', '4/6', '4/13', '4/20', '5/4', '5/11', '5/18', '6/1']

from collections import defaultdict
company_count = defaultdict(list)
for item in parsed_data:
    pd, pg, pn, pc, pt = item
    norm_c = str(pc).lower().replace(" ", "")
    if norm_c == "k-water": norm_c = "한국수자원공사"
    elif "코레일테크" in norm_c: norm_c = "코레일테크㈜"
    elif "경제통상" in norm_c: norm_c = "(재)대전경제통상진흥원"
    elif norm_c == "kt&g": norm_c = "KT&G"
    elif norm_c == "대산f&b": norm_c = "대산F&B"
    company_count[norm_c].append(item)

duplicates_norm = {k: v for k, v in company_count.items() if len(v) > 1}

from datetime import datetime
def parse_dt(s):
    try:
        return datetime.strptime(s.strip(), "%m.%d. %H:%M")
    except ValueError:
        return datetime.now()

duplicates_earliest = {}
for k, v in duplicates_norm.items():
    earliest = min(v, key=lambda x: parse_dt(x[4]))
    duplicates_earliest[k] = parse_dt(earliest[4])

schedule_obj = []
for d in dates:
    pubs = []
    pris = []
    
    for pd, pg, pn, pc, pt in parsed_data:
        if pd == d:
            norm_c = str(pc).lower().replace(" ", "")
            if norm_c == "k-water": norm_c = "한국수자원공사"
            elif "코레일테크" in norm_c: norm_c = "코레일테크㈜"
            elif "경제통상" in norm_c: norm_c = "(재)대전경제통상진흥원"
            elif norm_c == "kt&g": norm_c = "KT&G"
            elif norm_c == "대산f&b": norm_c = "대산F&B"
            
            error_msg = ""
            if pn == '유태수' and pd == '4/6':
                error_msg = "(6주차/4.13작성건)"
                
            if norm_c in duplicates_norm:
                others = [f"{o_pn}({o_pd})" for o_pd, o_pg, o_pn, o_pc, o_pt in duplicates_norm[norm_c] if o_pn != pn or o_pd != pd]
                if others:
                    if error_msg: error_msg += " | "
                    error_msg += f"중복선정: {', '.join(others)}와 동일"
                    
                    if parse_dt(pt) > duplicates_earliest[norm_c]:
                        error_msg += " (변경필요)"
                        pc = "변경 필요"
            
            entry = {"name": pn, "company": pc, "time": pt, "error": error_msg}
            if pg == '공공':
                pubs.append(entry)
            else:
                pris.append(entry)
                
    while len(pubs) < 4: pubs.append({"name": "", "company": "", "time": "", "error": ""})
    while len(pris) < 4: pris.append({"name": "", "company": "", "time": "", "error": ""})
    
    schedule_obj.append({"date": d, "public": pubs[:4], "private": pris[:4]})

html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>지역사회의 이해 발표 일정</title>
    <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-body: #f1f5f9;
            --surface: #ffffff;
            --border: #e2e8f0;
            --text-main: #1e293b;
            --text-muted: #64748b;
            --primary: #2563eb;
            --success: #10b981;
            --error: #ef4444;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Pretendard', sans-serif;
        }}

        body {{
            background-color: var(--bg-body);
            color: var(--text-main);
            padding: 1rem;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
        }}

        .header-section {{
            text-align: center;
            margin-bottom: 2rem;
        }}

        h1 {{
            font-size: 2rem;
            font-weight: 700;
            color: var(--text-main);
            margin-bottom: 0.5rem;
        }}

        .subtitle {{
            color: var(--text-muted);
            font-size: 1rem;
        }}

        .table-container {{
            width: 100%;
            max-width: 100%; /* Changed to essentially cover viewport width to avoid truncating long texts */
            margin: 0 1rem;
            background: var(--surface);
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
            overflow-x: auto;
            border: 1px solid var(--border);
        }} /* Adjusted for massive width display limit */

        table {{
            width: 100%;
            min-width: 1400px; /* Forces enough width inside container */
            border-collapse: collapse;
            text-align: left;
        }}

        th {{
            background-color: var(--bg-body);
            color: var(--text-muted);
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.85rem;
            letter-spacing: 0.05em;
            padding: 1rem 1.5rem;
            border-bottom: 2px solid var(--border);
        }}

        th:nth-child(1) {{ width: 80px; text-align: center; }}
        th:nth-child(2) {{ border-right: 1px solid var(--border); }}
        th:nth-child(3) {{ }}

        td {{
            padding: 1.5rem;
            border-bottom: 1px solid var(--border);
            vertical-align: top;
        }}

        td:nth-child(1) {{
            text-align: center;
            font-weight: 600;
            border-right: 1px solid var(--border);
            background: #fafaf9;
            vertical-align: middle;
            font-size: 1.1rem;
        }}

        td:nth-child(2) {{ border-right: 1px solid var(--border); }}

        tr:last-child td {{ border-bottom: none; }}

        tr:hover td:nth-child(2), tr:hover td:nth-child(3) {{
            background-color: #f8fafc;
        }}

        .slot-container {{
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
        }}

        .slot-wrapper {{
            display: flex;
            flex-direction: column;
        }}
        
        .slot {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
            position: relative;
        }}

        .slot-number {{
            color: var(--text-muted);
            font-size: 0.85rem;
            font-weight: 600;
            width: 16px;
            text-align: center;
        }}

        .input-group {{
            display: flex;
            flex: 1; /* stretches inside slot */
            gap: 0.5rem;
            background: #ffffff;
            border: 1px solid var(--border);
            border-radius: 6px;
            overflow: hidden;
            transition: border-color 0.2s, box-shadow 0.2s;
        }}

        .input-group:focus-within {{
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
        }}

        select {{
            flex: 7; /* Increased proportion of flex specifically for select to keep text from truncating */
            min-width: 0;
            border: none;
            padding: 0.5rem 2rem 0.5rem 0.75rem; /* Space reserved only where the arrow rests */
            outline: none;
            color: var(--text-main);
            background: transparent;
            font-size: 0.95rem;
            font-weight: 500;
            cursor: pointer;
            border-right: 1px solid var(--border);
            appearance: none;
            background-image: url("data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20stroke%3D%22%2394a3b8%22%20stroke-width%3D%222%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%3E%3Cpolyline%20points%3D%226%209%2012%2015%2018%209%22%3E%3C%2Fpolyline%3E%3C%2Fsvg%3E");
            background-repeat: no-repeat;
            background-position: right 0.5rem center; /* Adjusted arrow position closely to the right edge */
            background-size: 1.2em;
            text-overflow: ellipsis; 
            /* Kept ellipsis incase of super long outlier but gave it 7 times the flex area */
        }}

        input {{
            flex: 2;
            min-width: 0;
            border: none;
            padding: 0.5rem 0.2rem 0.5rem 0.5rem;
            outline: none;
            color: var(--text-main);
            background: transparent;
            font-size: 0.95rem;
        }}

        .time-tag {{
            color: #94a3b8;
            font-size: 0.8rem;
            padding-right: 0.5rem;
            font-weight: 500;
            white-space: nowrap;
            width: 85px;
            text-align: right;
            display: flex;
            align-items: center;
            justify-content: flex-end;
        }}

        input::placeholder {{
            color: #cbd5e1;
        }}

        .error-tag {{
            display: inline-block;
            background: rgba(239, 68, 68, 0.1);
            color: var(--error);
            font-size: 0.8rem;
            font-weight: 600;
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            margin-top: 4px;
            margin-left: 28px; /* sync with slot-number offset */
        }}

        @media (max-width: 768px) {{
            th, td {{ padding: 1rem 0.75rem; }}
            .input-group {{ flex-direction: column; gap: 0; }}
            select {{ border-right: none; border-bottom: 1px solid var(--border); }}
        }}
    </style>
</head>
<body>

    <div class="header-section">
        <h1>발표 일정 테이블</h1>
        <p class="subtitle">공공기관 4명, 상장기업 4명 슬롯 지정 양식</p>
    </div>

    <div class="table-container">
        <table>
            <thead>
                <tr>
                    <th>날짜</th>
                    <th>공공기관</th>
                    <th>상장기업</th>
                </tr>
            </thead>
            <tbody id="tbody">
            </tbody>
        </table>
    </div>

    <script>
        const companies = {json.dumps(all_companies, ensure_ascii=False)};
        const schedule = {json.dumps(schedule_obj, ensure_ascii=False)};
        const occupiedCompanies = new Set();
        
        schedule.forEach(day => {{
            day.public.forEach(slot => {{ if(slot.company && slot.company !== '변경 필요') occupiedCompanies.add(slot.company); }});
            day.private.forEach(slot => {{ if(slot.company && slot.company !== '변경 필요') occupiedCompanies.add(slot.company); }});
        }});

        function generateOptions(selectedValue) {{
            let options = `<option value="" ${{selectedValue === '' ? 'selected' : ''}}>선택 안함</option>`;
            let found = false;
            companies.forEach(company => {{
                const isSelected = company === selectedValue ? 'selected' : '';
                const isOccupied = occupiedCompanies.has(company) && company !== selectedValue;
                const styleAttr = isOccupied ? ' style="text-decoration: line-through; color: #a1a1aa;" disabled' : '';
                
                if(isSelected) found = true;
                options += `<option value="${{company}}"${{styleAttr}} ${{isSelected}}>${{company}}</option>`;
            }});
            
            if (selectedValue && selectedValue !== '' && !found) {{
                options += `<option value="${{selectedValue}}" selected>${{selectedValue}}</option>`;
            }}
            return options;
        }}

        function refreshDropdowns() {{
            const selects = document.querySelectorAll('select');
            const selectedSet = new Set();
            
            selects.forEach(s => {{
                if (s.value && s.value !== '변경 필요' && s.value !== '선택 안함') {{
                    selectedSet.add(s.value);
                }}
            }});

            selects.forEach(s => {{
                const currentVal = s.value;
                Array.from(s.options).forEach(opt => {{
                    if (!opt.value || opt.value === '변경 필요') return;

                    if (selectedSet.has(opt.value) && opt.value !== currentVal) {{
                        opt.style.textDecoration = 'line-through';
                        opt.style.color = '#a1a1aa';
                        opt.disabled = true;
                    }} else {{
                        opt.style.textDecoration = 'none';
                        opt.style.color = '';
                        opt.disabled = false;
                    }}
                }});
            }});
        }}

        function createSlotsHtml(slotsArray) {{
            return `
                <div class="slot-container">
                    ${{slotsArray.map((slot, i) => `
                        <div class="slot-wrapper">
                            <div class="slot">
                                <span class="slot-number">${{i+1}}</span>
                                <div class="input-group">
                                    <select title="기업 선택" onchange="refreshDropdowns()">
                                        ${{generateOptions(slot.company)}}
                                    </select>
                                    <input type="text" placeholder="이름 입력" value="${{slot.name}}">
                                    <div class="time-tag">${{slot.time || '&nbsp;'}}</div>
                                </div>
                            </div>
                            ${{slot.error ? `<span class="error-tag">${{slot.error}}</span>` : ''}}
                        </div>
                    `).join('')}}
                </div>
            `;
        }}

        const tbody = document.getElementById('tbody');

        schedule.forEach(day => {{
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${{day.date}}</td>
                <td>
                    ${{createSlotsHtml(day.public)}}
                </td>
                <td>
                    ${{createSlotsHtml(day.private)}}
                </td>
            `;
            tbody.appendChild(tr);
        }});
    </script>
</body>
</html>
"""

with open('c:/Users/Sumin/00_Projects/지역사회의이해발표시트/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
