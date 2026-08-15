-- 1. 查看 users 表里的所有数据
SELECT * FROM users;

-- 2. 统计 users 表一共有多少条数据
SELECT COUNT(*) AS total_users
FROM users;

-- 3. 只查看我们需要的几个字段
SELECT name, email, city
FROM users;