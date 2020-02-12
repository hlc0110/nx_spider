-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2020-02-12 16:37:54
-- 服务器版本： 5.6.26
-- PHP 版本： 7.3.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `cl`
--

-- --------------------------------------------------------

--
-- 表的结构 `app`
--

CREATE TABLE `app` (
  `id` int(11) UNSIGNED NOT NULL,
  `app_name` varchar(255) COLLATE utf8mb4_bin NOT NULL COMMENT '应用名',
  `intro` text COLLATE utf8mb4_bin NOT NULL COMMENT '简介',
  `link` varchar(500) COLLATE utf8mb4_bin NOT NULL COMMENT '链接'
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- 表的结构 `review`
--

CREATE TABLE `review` (
  `app_id` int(11) NOT NULL COMMENT '应用id',
  `comment` text COLLATE utf8mb4_bin NOT NULL COMMENT '评论内容',
  `language` tinyint(2) NOT NULL COMMENT '评论语言',
  `other` varchar(255) COLLATE utf8mb4_bin NOT NULL COMMENT '其他信息'
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- 转储表的索引
--

--
-- 表的索引 `app`
--
ALTER TABLE `app`
  ADD PRIMARY KEY (`id`);

--
-- 表的索引 `review`
--
ALTER TABLE `review`
  ADD KEY `app_id` (`app_id`),
  ADD KEY `language` (`language`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `app`
--
ALTER TABLE `app`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
