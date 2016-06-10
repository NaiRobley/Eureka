-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 29, 2016 at 11:19 PM
-- Server version: 5.7.11-0ubuntu6
-- PHP Version: 7.0.5-3+donate.sury.org~xenial+1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `eureka`
--
CREATE DATABASE IF NOT EXISTS `eureka` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `eureka`;

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--
-- Creation: Apr 23, 2016 at 09:01 AM
--

DROP TABLE IF EXISTS `admins`;
CREATE TABLE `admins` (
  `au_id` int(11) NOT NULL,
  `auname` varchar(256) NOT NULL,
  `apasswd` varchar(256) NOT NULL,
  `aemail` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- RELATIONS FOR TABLE `admins`:
--

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`au_id`, `auname`, `apasswd`, `aemail`) VALUES
(1, 'robley', 'robley', 'robley@admin.com'),
(2, 'root', 'root', 'root@eureka.com');

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--
-- Creation: Apr 28, 2016 at 10:35 PM
--

DROP TABLE IF EXISTS `categories`;
CREATE TABLE `categories` (
  `c_id` int(11) NOT NULL,
  `cname` varchar(256) NOT NULL,
  `cdesc` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- RELATIONS FOR TABLE `categories`:
--

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`c_id`, `cname`, `cdesc`) VALUES
(1, 'Computer Science', 'This category contains projects in the field of Computer Science. It includes projects that deal with hardware as well as software.'),
(2, 'Business', 'This category contains projects in the field of Business. It is addressed to those willing and eager to learn about enterprenuership.'),
(3, 'Engineering', 'This category contains projects in the field of Engineering. It includes projects that deal with hardware that changes the way we do things by employing skills of engineering.'),
(4, 'Other', 'This category contains projects that cannot be classified in the other fields above. Kindly note that more categories will be added and those with projects will be allowed to edit their projects and change the category of their project as appropriate.');

-- --------------------------------------------------------

--
-- Table structure for table `projects`
--
-- Creation: Apr 28, 2016 at 10:39 PM
-- Last update: Apr 28, 2016 at 10:59 PM
--

DROP TABLE IF EXISTS `projects`;
CREATE TABLE `projects` (
  `p_id` int(11) NOT NULL,
  `pname` varchar(256) NOT NULL,
  `pdesc` varchar(256) NOT NULL,
  `c_id` int(11) NOT NULL,
  `u_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- RELATIONS FOR TABLE `projects`:
--   `u_id`
--       `users` -> `u_id`
--   `c_id`
--       `categories` -> `c_id`
--

--
-- Dumping data for table `projects`
--

INSERT INTO `projects` (`p_id`, `pname`, `pdesc`, `c_id`, `u_id`) VALUES
(1, 'First Computer Science Project', 'Lorem ipsum dolor sit amet, consectetur adipiariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 1, 12),
(2, 'Business Project', 'Cras sit amet pulvinar dolor. Vivamus sit amet lacinia leo, eget interdum leo. Sed faucibus libero sapien, sit amet hendrerit tortor semper quis. Nullam vulputate ligula elit, nec rutrum augue auctor quis.', 2, 1),
(3, 'Other Project', 'Pellentesque tristique ante in neque placerat vestibulum. Nunc efficitur nibh et nisl sagittis scelerisque. Duis sodales consectetur leo nec faucibus.', 4, 1),
(4, 'Morbi id project', 'Morbi id imperdiet mi. Quisque consequat, eros sit amet mollis varius, magna ipsum maximus turpis, sed dapibus diam leo at mauris. ', 2, 1),
(5, 'Engineering Project', 'Nulla sed tellus ut elit cursus commodo. Pellentesque in cursus nisi. Aenean in dui neque. Fusce mauris risus, ullamcorper ut leo sed, vel scelerisque dui elit eu nisl.', 3, 1),
(6, 'Other Project', 'Nullam tincidunt feugiat ipsum, id malesuada urna mollis vitae. Nullam lacinia ante odio, quis euismod nibh elementum nec.\n\nVestibulum mollis vestibulum nunc, ut malesuada sem tempus a.', 4, 1),
(7, 'Vestibulum dui purus', 'Vestibulum dui purus, scelerisque et ipsum vitae, mollis finibus orci. Aenean viverra orci pretium lacinia fermentum. Integer congue urna a nisl finibus porttitor.', 1, 2),
(8, 'Efficitur project', 'Phasellus efficitur erat non pretium ultrices. Etiam viverra justo dolor, a fermentum dui hendrerit eget. Ut convallis ante ut vestibulum varius.', 1, 1),
(9, 'Maecenas sagittis project', 'Maecenas sagittis dignissim felis a pulvinar. Donec nec orci viverra quam tristique molestie. Etiam a porta tellus, nec blandit lectus.', 4, 12),
(11, 'Eleifend project', 'Nam at eleifend risus. Quisque at dui at magna pharetra euismod at at sem. Sed dictum odio eget diam porttitor feugiat. ', 2, 3),
(12, 'Asus Project', 'Vivamus sit amet lacinia leo, eget interdum leo. Sed faucibus libero sapien, sit amet hendrerit tortor semper quis. Nullam vulputate ligula elit, nec rutrum augue auctor quis', 1, 13),
(13, 'Semper project', 'Donec interdum semper leo, a sodales tellus tristique volutpat. Aliquam laoreet quis justo laoreet condimentum. In hac habitasse platea dictumst.', 1, 1),
(14, 'Ipsum Project', 'Quisque in mi eget ipsum hendrerit lacinia vitae id turpis. Interdum et malesuada fames ac ante ipsum primis in faucibus. ', 1, 1),
(15, 'This is an engineering project', 'Cras sit amet pulvinar dolor. Vivamus sit amet lacinia leo, eget interdum leo. Sed faucibus libero sapien, sit amet hendrerit tortor semper quis. Nullam vulputate ligula elit, nec rutrum augue auctor quis.', 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--
-- Creation: Apr 23, 2016 at 09:01 AM
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `u_id` int(11) NOT NULL,
  `fname` varchar(256) NOT NULL,
  `lname` varchar(256) NOT NULL,
  `email` varchar(256) NOT NULL,
  `gender` varchar(256) NOT NULL,
  `u_name` varchar(256) NOT NULL,
  `password` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- RELATIONS FOR TABLE `users`:
--

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`u_id`, `fname`, `lname`, `email`, `gender`, `u_name`, `password`) VALUES
(1, 'Robley', 'Gori', 'rob@ley.com', 'male', 'robley', 'robley'),
(2, 'A', 'B', 'c@d.e', 'male', 'f', 'g'),
(3, 'Faith', 'Kerubo', 'faith@kerubo.com', 'female', 'faith', 'kerubo'),
(9, 'First', 'Last', 'email@email.com', 'male', 'first', 'last'),
(10, 'Hhe', 'Haha', 'ha@ha.ha', 'male', 'haha', 'haha'),
(11, 'hehe', 'hehe', 'h@e.e', 'female', 'hehehe', 'hhheee'),
(12, 'Sharon', 'Waithira', 'sharon@syra.com', 'female', 'syra', 'syra'),
(13, 'Asus', 'Zenfon', 'asus@zenfon.com', 'male', 'asus', 'asus');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`au_id`);

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`c_id`),
  ADD KEY `c_id` (`c_id`);

--
-- Indexes for table `projects`
--
ALTER TABLE `projects`
  ADD PRIMARY KEY (`p_id`),
  ADD KEY `u_id` (`u_id`),
  ADD KEY `c_id` (`c_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`u_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admins`
--
ALTER TABLE `admins`
  MODIFY `au_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `projects`
--
ALTER TABLE `projects`
  MODIFY `p_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `u_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `projects`
--
ALTER TABLE `projects`
  ADD CONSTRAINT `projects_ibfk_1` FOREIGN KEY (`u_id`) REFERENCES `users` (`u_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `projects_ibfk_2` FOREIGN KEY (`c_id`) REFERENCES `categories` (`c_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
