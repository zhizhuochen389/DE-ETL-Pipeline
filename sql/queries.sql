-- 1. 查看 users 表里的所有数据
SELECT * FROM users;

-- 2. 统计 users 表一共有多少条数据
SELECT COUNT(*) AS total_users
FROM users;

-- 3. 只查看我们需要的几个字段
SELECT name, email, city
FROM users;
-- 4. Check for missing critical fields
SELECT *
FROM users
WHERE name IS NULL
   OR email IS NULL
   OR city IS NULL;

-- 5. Count users by city
SELECT city, COUNT(*) AS user_count
FROM users
GROUP BY city
ORDER BY user_count DESC;

-- 6. View users ordered by id
SELECT id, name, username, email, city
FROM users
ORDER BY id;