-- desription
SELECT COLUMN_NAME, DATA_TYPE, COLUMN_TYPE 
FROM information_schema.COLUMNS 
WHERE TABLE_SCHEMA = 'hbtn_0c_0' 
  AND TABLE_NAME = 'first_table';