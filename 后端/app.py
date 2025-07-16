import os
import json
import csv
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app, supports_credentials=True)

USER_FILE = 'users.json'
GOALS_FILE = 'goals.json'
WEIGHTS_FILE = 'weights.json'
PUNCH_FILE = 'punch.json'
PROFILE_FILE = 'profile.json'

def load_json(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 新增成就系统逻辑
def add_achievement(user_id, title, description):
    all_profiles = load_json(PROFILE_FILE)
    profile = all_profiles.get(user_id, {})
    achievements = profile.get('achievements', [])

    # 检查是否已经获得该成就
    for achievement in achievements:
        if achievement['title'] == title:
            return

    # 添加新成就
    achievement = {
        "title": title,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d")
    }
    achievements.append(achievement)
    profile['achievements'] = achievements
    all_profiles[user_id] = profile
    save_json(PROFILE_FILE, all_profiles)

# 用户注册
@app.route('/register', methods=['POST'])
def register():
    user_db = load_json(USER_FILE)
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'msg': '请填写所有字段'}), 400
    if username in user_db:
        return jsonify({'msg': '用户名已存在'}), 409
    user_db[username] = password
    save_json(USER_FILE, user_db)

    # 初始化用户 profile 数据
    all_profiles = load_json(PROFILE_FILE)
    all_profiles[username] = {
        "nickname": "未命名用户",
        "avatar": "/static/avatar-default.png",
        "signature": "健康每一天！",
        "achievements": []
    }
    save_json(PROFILE_FILE, all_profiles)

    return jsonify({'msg': '注册成功'})

# 用户登录
@app.route('/login', methods=['POST'])
def login():
    user_db = load_json(USER_FILE)
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'msg': '请输入用户名和密码'}), 400
    if username in user_db and user_db[username] == password:
        return jsonify({'msg': '登录成功'})
    return jsonify({'msg': '用户名或密码错误'}), 401

# 获取运动计划
@app.route('/api/goals', methods=['GET'])
def get_goals():
    user_id = request.args.get('user_id')
    all_goals = load_json(GOALS_FILE)
    return jsonify({'goals': all_goals.get(user_id, [])})

# 新增或编辑运动计划
@app.route('/api/goals', methods=['POST'])
def add_or_update_goal():
    all_goals = load_json(GOALS_FILE)
    data = request.get_json()
    user_id = data.get('user_id')
    if not user_id:
        return jsonify({'msg': '缺少用户信息'}), 400
    plan = dict(data)
    user_goals = all_goals.get(user_id, [])
    # 编辑
    if plan.get('id'):
        for idx, p in enumerate(user_goals):
            if p['id'] == plan['id']:
                user_goals[idx] = plan
                all_goals[user_id] = user_goals
                save_json(GOALS_FILE, all_goals)
                return jsonify({'msg': '修改成功'})
        user_goals.append(plan)
        all_goals[user_id] = user_goals
        save_json(GOALS_FILE, all_goals)
        return jsonify({'msg': '添加成功'})
    else:
        import time
        plan['id'] = int(time.time() * 1000)
        user_goals.append(plan)
        all_goals[user_id] = user_goals
        save_json(GOALS_FILE, all_goals)
        return jsonify({'msg': '添加成功'})

# 删除运动计划
@app.route('/api/goals/<int:plan_id>', methods=['DELETE'])
def delete_goal(plan_id):
    all_goals = load_json(GOALS_FILE)
    user_id = request.json.get('user_id')
    user_goals = all_goals.get(user_id, [])
    before = len(user_goals)
    user_goals = [plan for plan in user_goals if plan['id'] != plan_id]
    all_goals[user_id] = user_goals
    save_json(GOALS_FILE, all_goals)
    after = len(user_goals)
    if before == after:
        return jsonify({'msg': '未找到该计划'}), 404
    return jsonify({'msg': '删除成功'})

# 获取体重目标
@app.route('/api/weight', methods=['GET'])
def get_weight():
    user_id = request.args.get('user_id')
    all_weights = load_json(WEIGHTS_FILE)
    return jsonify({'weight': all_weights.get(user_id, '')})

# 设置体重目标
@app.route('/api/weight', methods=['POST'])
def set_weight():
    all_weights = load_json(WEIGHTS_FILE)
    data = request.get_json()
    user_id = data.get('user_id')
    weight = data.get('weight')
    if not user_id or not weight:
        return jsonify({'msg': '缺少参数'}), 400
    all_weights[user_id] = weight
    save_json(WEIGHTS_FILE, all_weights)
    return jsonify({'msg': '设置成功'})

# 获取打卡记录
@app.route('/api/punch', methods=['GET'])
def get_punch():
    user_id = request.args.get('user_id')
    all_punch = load_json(PUNCH_FILE)
    punchDates = all_punch.get(user_id, [])
    return jsonify({'punchDates': punchDates})

# 打卡接口中增加成就逻辑
@app.route('/api/punch', methods=['POST'])
def post_punch():
    all_punch = load_json(PUNCH_FILE)
    data = request.get_json()
    user_id = data.get('user_id')
    date = data.get('date')
    if not user_id or not date:
        return jsonify({'msg': '缺少参数'}), 400
    punchDates = set(all_punch.get(user_id, []))
    if date in punchDates:
        return jsonify({'msg': '今日已打卡'}), 200
    punchDates.add(date)
    all_punch[user_id] = list(punchDates)
    save_json(PUNCH_FILE, all_punch)

    # 确保用户在 profile.json 中有 achievements 字段
    all_profiles = load_json(PROFILE_FILE)
    profile = all_profiles.get(user_id, {})
    if 'achievements' not in profile:
        profile['achievements'] = []

    # 计算连续打卡天数
    punchDates = sorted(punchDates)
    maxStreak = 0
    currentStreak = 0
    last_date = None

    for d in punchDates:
        if last_date and (datetime.strptime(d, "%Y-%m-%d") - datetime.strptime(last_date, "%Y-%m-%d")).days == 1:
            currentStreak += 1
        else:
            currentStreak = 1
        maxStreak = max(maxStreak, currentStreak)
        last_date = d

    # 检查成就条件
    if currentStreak == 1:
        add_achievement(user_id, "首次打卡", "恭喜你完成了首次打卡！")
    elif currentStreak == 3:
        add_achievement(user_id, "连续打卡3天", "恭喜你连续打卡3天！")
    elif currentStreak == 7:
        add_achievement(user_id, "连续打卡7天", "恭喜你连续打卡7天！")
    elif currentStreak == 10:
        add_achievement(user_id, "连续打卡10天", "恭喜你连续打卡10天！")
    elif currentStreak == 15:
        add_achievement(user_id, "连续打卡15天", "恭喜你连续打卡15天！")
    elif currentStreak == 30:
        add_achievement(user_id, "连续打卡30天", "恭喜你连续打卡30天！")

    return jsonify({'msg': '打卡成功'})

# 个人资料相关（含BMI参数）
@app.route('/api/profile', methods=['GET'])
def get_profile():
    user_id = request.args.get('user_id')
    all_profiles = load_json(PROFILE_FILE)
    return jsonify({'profile': all_profiles.get(user_id, {})})

@app.route('/api/profile', methods=['POST'])
def update_profile():
    all_profiles = load_json(PROFILE_FILE)
    data = request.get_json()
    user_id = data.get('user_id')
    if not user_id:
        return jsonify({'msg': '缺少用户'}), 400
    profile = all_profiles.get(user_id, {})
    # 支持昵称、头像、签名、BMI参数
    for k in ['nickname', 'avatar', 'signature', 'bmi_height', 'bmi_weight', 'targetHeight', 'targetWeight']:
        if k in data:
            profile[k] = data[k]
    all_profiles[user_id] = profile
    save_json(PROFILE_FILE, all_profiles)
    return jsonify({'msg': '保存成功'})

# 更改密码
@app.route('/api/profile/password', methods=['POST'])
def update_password():
    user_db = load_json(USER_FILE)
    data = request.get_json()
    user_id = data.get('user_id')
    password = data.get('password')
    if not user_id or not password:
        return jsonify({'msg': '缺少参数'}), 400
    if user_id not in user_db:
        return jsonify({'msg': '用户不存在'}), 404
    user_db[user_id] = password
    save_json(USER_FILE, user_db)
    return jsonify({'msg': '密码已修改'})

# 成就列表
@app.route('/api/achievements', methods=['GET'])
def get_achievements():
    user_id = request.args.get('user_id')
    all_profiles = load_json(PROFILE_FILE)
    profile = all_profiles.get(user_id, {})
    achievements = profile.get('achievements', [])
    return jsonify({'achievements': achievements})

# 统计分析接口
@app.route('/api/analysis', methods=['GET'])
def analysis():
    user_id = request.args.get('user_id')
    trend_tab = int(request.args.get('trendTab', 0))
    # 拉取打卡记录
    punch_data = load_json(PUNCH_FILE)
    punch_dates = punch_data.get(user_id, [])
    punch_dates = sorted(punch_dates)
    # 拉取计划
    goals = load_json(GOALS_FILE).get(user_id, [])

    # 1. 打卡趋势
    today = datetime.now()
    if trend_tab == 0:  # 近7天
        days = [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(6, -1, -1)]
    elif trend_tab == 1:  # 近30天
        days = [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(29, -1, -1)]
    elif trend_tab == 2:  # 本月
        y, m = today.year, today.month
        if m < 12:
            days = [f"{y}-{m:02d}-{d:02d}" for d in range(1, (datetime(y, m + 1, 1) - timedelta(days=1)).day + 1)]
        else:
            days = [f"{y}-{m:02d}-{d:02d}" for d in range(1, (datetime(y + 1, 1, 1) - timedelta(days=1)).day + 1)]
    else:  # 全年
        y = today.year
        days = [f"{y}-{m:02d}" for m in range(1, 13)]
    by_day = {}
    for d in punch_dates:
        if trend_tab < 3:
            by_day[d] = by_day.get(d, 0) + 1
        else:  # 全年，按月
            m = d[:7]
            by_day[m] = by_day.get(m, 0) + 1
    trend_arr = [by_day.get(d, 0) for d in days]
    trendChartData = {
        "categories": [d[5:] if trend_tab < 3 else d[5:] + "月" for d in days],
        "series": [{"name": "打卡次数", "data": trend_arr}]
    }

    # 2. 项目分布饼图
    project_count = {}
    for plan in goals:
        proj = plan.get("project")
        if proj:
            project_count[proj] = project_count.get(proj, 0) + 1
    pieChartData = {
        "series": [{"name": k, "data": v} for k, v in project_count.items()] or [{"name": "暂无数据", "data": 1}]
    }

    # 3. 目标完成率（本月目标天数/实际打卡天数）
    this_month = today.strftime("%Y-%m")
    this_month_days = [d for d in punch_dates if d.startswith(this_month)]
    month_goal_days = 20
    goalRate = min(1, len(this_month_days) / month_goal_days) if month_goal_days else 0

    # 4. 统计：最长连续打卡、最佳月、平均每周、最爱项目
    maxStreak, curStreak, last = 0, 0, ''
    for d in punch_dates:
        if last and (datetime.strptime(d, "%Y-%m-%d") - datetime.strptime(last, "%Y-%m-%d")).days == 1:
            curStreak += 1
        else:
            curStreak = 1
        maxStreak = max(maxStreak, curStreak)
        last = d

    # 最佳月
    month_map = {}
    for d in punch_dates:
        m = d[:7]
        month_map[m] = month_map.get(m, 0) + 1
    bestMonth = max(month_map.values()) if month_map else 0
    # 平均每周
    week_map = {}
    for d in punch_dates:
        y, m, dd = map(int, d.split('-'))
        dt = datetime(y, m, dd)
        week = dt.isocalendar()[1]
        key = f"{y}-W{week}"
        week_map[key] = week_map.get(key, 0) + 1
    avgWeekTimes = round(sum(week_map.values()) / len(week_map), 1) if week_map else 0
    # 最爱项目
    favoriteProject = max(project_count, key=project_count.get) if project_count else ''
    # 智能建议
    suggestion = "请继续保持锻炼习惯！" if goalRate > 0.6 else "建议加强锻炼频率，争取达成目标～"

    return jsonify({
        "trendChartData": trendChartData,
        "pieChartData": pieChartData,
        "goalRate": goalRate,
        "maxStreak": maxStreak,
        "bestMonth": bestMonth,
        "avgWeekTimes": avgWeekTimes,
        "favoriteProject": favoriteProject,
        "suggestion": suggestion
    })

# 导出CSV报告
@app.route('/api/export', methods=['GET'])
def export_csv():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'msg': '缺少用户信息'}), 400

    # 获取打卡记录
    punch_data = load_json(PUNCH_FILE)
    punch_dates = punch_data.get(user_id, [])

    # 获取运动计划
    goals_data = load_json(GOALS_FILE)
    goals = goals_data.get(user_id, [])

    # 创建CSV文件
    csv_file_path = f"{user_id}_fitness_report.csv"
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)

        # 写入打卡记录
        csvwriter.writerow(['Date', 'Punched'])
        for date in punch_dates:
            csvwriter.writerow([date, 'Yes'])

        # 写入运动计划
        csvwriter.writerow(['', '', ''])
        csvwriter.writerow(['Goal ID', 'Project', 'Description'])
        for goal in goals:
            csvwriter.writerow([goal.get('id', ''), goal.get('project', ''), goal.get('description', '')])

    # 返回CSV文件
    return send_file(csv_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)