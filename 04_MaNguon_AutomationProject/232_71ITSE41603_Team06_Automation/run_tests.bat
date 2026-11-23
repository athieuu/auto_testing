@echo off
chcp 65001 > nul
set JAVA_HOME=C:\Program Files\Java\jdk-23
echo ========================================================
echo   KIỂM THỬ TỰ ĐỘNG - ĐỒ ÁN NHÓM TEAM 06 (LỚP 232_71ITSE41603_0102)
echo   HỆ THỐNG: QUẢN LÝ PHÂN CÔNG GIẢNG DẠY (VAI TRÒ BCN KHOA)
echo ========================================================
D:\ktdt\maven_tool\apache-maven-3.9.6\bin\mvn.cmd test
pause
