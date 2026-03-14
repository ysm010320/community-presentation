import json
import urllib.request
from collections import defaultdict

# Supabase configuration
SUPABASE_URL = "https://tduvcakgpburarevgubr.supabase.co/rest/v1"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRkdXZjYWtncGJ1cmFyZXZndWJyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzMzODk0NDIsImV4cCI6MjA4ODk2NTQ0Mn0.tR0CwvI-JMCT7n947fUhk7kc7ghBulNVGmCed_LHmfM"

TABLE_NAME = "presentations"

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
    ('5/11', '공공', ' 한성경', '한국산림복지진흥원', '5.5. 23:25'),
    ('5/11', '공공', '이채원', '대전창조경제혁신센터', '5.5. 23:36'),
    ('5/18', '상장', '양하영', '알루코', '5.10. 12:41'),
    ('5/18', '공공', '정현준', '한국화학연구원', '5.10. 12:43'),
    ('5/18', '상장', '정하진', '원텍', '5.10. 21:30'),
    ('5/18', '공공', '정구영', '한국수자원공사', '5.11. 11:21'),
    ('5/18', '상장', '이채원', '네오팜', '5.12. 12:53'),
    ('5/18', '공공', '전은재', '한국기계연구원', '5.12. 12:56'),
    ('5/18', '공공', '곽현지', '(재)대전경제통상진흥원', '5.13. 12:56'),
    ('6/1', '상장', '구민경', '컨텍', '5.24. 13:51'),
    ('6/1', '공공', '구민경', '연구개발특구진흥재단', '5.24. 13:51'),
    ('6/1', '공공', '양예지', '대전도시공사', '5.24. 13:52'),
    ('6/1', '상장', '양예지', '레인보우로보틱스', '5.24. 13:52'),
    ('6/1', '상장', '신재민', '파이버프로', '5.24. 13:53'),
    ('6/1', '공공', '신재민', '한국전력기술㈜ 원자로설계개발단', '5.24. 13:53'),
    ('6/1', '공공', '함석현', '금강유역환경청', '5.24. 13:58'),
    ('6/1', '상장', '함석현', '나노신소재', '5.24. 13:58'),
    ('6/1', '공공', '임지선', '국립중앙과학관', '5.24. 14:02'),
    ('6/1', '상장', '임지선', '나노팀', '5.24. 14:02'),
    ('6/1', '공공', '이유진', '대전인재개발원', '5.24. 14:03'),
    ('6/1', '상장', '이유진', '나노엔텍', '5.24. 14:03'),
    ('6/1', '공공', '임정빈', '대전교육정보원', '5.24. 14:04'),
    ('6/1', '상장', '임정빈', '노타', '5.24. 14:04'),
    ('6/1', '공공', '김희진', '화학물질안전원', '5.24. 14:05'),
    ('6/1', '상장', '김희진', '뉴로스', '5.24. 14:05'),
    ('6/1', '공공', '이도현', '대전광역시 시설관리공단 무지개복지센터', '5.24. 14:07'),
    ('6/1', '상장', '이도현', '디엔에프', '5.24. 14:07'),
    ('6/1', '공공', '김지현', '연구개발특구진흥재단', '5.25. 10:14'),
    ('6/1', '상장', '김지현', '라이온켐텍', '5.25. 10:14'),
    ('5/11', '공공', '조인서', '한국한의학연구원', '5.12. 23:44'),
    ('5/11', '상장', '조인서', 'HLB제넥스', '5.12. 23:44')
]

dates = ['3/23', '3/30', '4/6', '4/13', '4/20', '5/4', '5/11', '5/18', '6/1']

# Normalization and Duplicate Check logic (Simplified for seeding)
company_count = defaultdict(list)
for item in parsed_data:
    pd, pg, pn, pc, pt = item
    norm_c = str(pc).lower().replace(" ", "")
    if norm_c == "k-water": norm_c = "한국수자원공사"
    elif "코레일테크" in norm_c: norm_c = "코레일테크㈜"
    elif "경제통상" in norm_c: norm_c = "(재)대전경제통상진흥원"
    elif norm_c == "kt&g": norm_c = "KT&G"
    elif norm_c == "대산f&b": norm_c = "대산F&B"
    company_count[norm_c].append(pt)

duplicates_earliest = {}
for comp, times in company_count.items():
    if len(times) > 1:
        times_parsed = []
        for t in times:
            try:
                import datetime
                tp = datetime.datetime.strptime(t.strip(), "%m.%d. %H:%M")
                times_parsed.append(tp)
            except: pass
        if times_parsed:
            duplicates_earliest[comp] = min(times_parsed)

to_insert = []
# Group by date and category to ensure 4 slots
grouped = defaultdict(lambda: {'공공': [], '상장': []})
for d, g, n, c, t in parsed_data:
    err = ""
    norm_c = str(c).lower().replace(" ", "")
    # Add normalization here too for consistency
    if norm_c == "k-water": norm_c = "한국수자원공사"
    elif "코레일테크" in norm_c: norm_c = "코레일테크㈜"
    elif "경제통상" in norm_c: norm_c = "(재)대전경제통상진흥원"
    elif norm_c == "kt&g": norm_c = "KT&G"
    elif norm_c == "대산f&b": norm_c = "대산F&B"
    
    if norm_c in duplicates_earliest:
        try:
            import datetime
            tp = datetime.datetime.strptime(t.strip(), "%m.%d. %H:%M")
            if tp > duplicates_earliest[norm_c]:
                err = "(변경필요)"
        except: pass
    
    grouped[d][g].append({
        "name": n,
        "company": "변경 필요" if "(변경필요)" in err else c,
        "comment_time": t,
        "error_msg": err
    })

for d in dates:
    for g in ['공공', '상장']:
        slots = grouped[d][g]
        while len(slots) < 4:
            slots.append({"name": "", "company": "", "comment_time": "", "error_msg": ""})
        
        for i, s in enumerate(slots):
            to_insert.append({
                "date": d,
                "category": g,
                "slot_index": i + 1,
                "name": s["name"],
                "company": s["company"],
                "comment_time": s["comment_time"],
                "error_msg": s["error_msg"]
            })

# note: Supabase REST API via PostgREST
headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

url = f"{SUPABASE_URL}/{TABLE_NAME}"

# Step 1: Clear existing data
try:
    print("Clearing existing data...")
    # PostgREST often requires a filter for DELETE to prevent accidental full-table wipes.
    # We use a filter that matches all likely dates.
    req_del = urllib.request.Request(f"{url}?date=neq.0", headers=headers, method="DELETE")
    with urllib.request.urlopen(req_del) as res:
        print(f"Delete Status: {res.status}")
except Exception as e:
    print(f"Delete Error: {e}")
    if hasattr(e, 'read'):
        print(e.read().decode())

# Step 2: Insert new data
try:
    print("Migrating new data...")
    req = urllib.request.Request(url, data=json.dumps(to_insert).encode(), headers=headers, method="POST")
    with urllib.request.urlopen(req) as res:
        print(f"Insert Status: {res.status}")
        print("Data successfully migrated to Supabase.")
except Exception as e:
    print(f"Insert Error: {e}")
    if hasattr(e, 'read'):
        print(e.read().decode())
