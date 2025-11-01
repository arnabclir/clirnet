Update timestamp-

UPDATE `clirnet-dev.request_edit.H_5902_distinct_data`

SET timestamp = TIMESTAMP(DATETIME('2025-04-25', TIME(timestamp))),

logName = 'H_5902_distinct_2025-04-25'

WHERE DATE(timestamp) BETWEEN '2025-04-01' AND '2025-04-21'



UPDATE `clirnet-dev.request_edit.H_5902_distinct_data`

SET timestamp = TIMESTAMP(DATETIME('2025-04-25', TIME(timestamp))),

logName = 'H_5902_distinct_2025-04-25'

WHERE logName = 'add-report-prod-server'



UPDATE `clirnet-dev.request_edit.H_5902_distinct_data`

SET timestamp = TIMESTAMP(DATETIME('2025-04-26', TIME(timestamp))),

logName = 'H_5902_distinct_2025-04-26'

WHERE DATE(timestamp) BETWEEN '2025-04-22' AND '2025-04-24' AND logName NOT IN ('H_5902_distinct_2025-04-25')



UPDATE `clirnet-dev.request_edit.H_5902_distinct_data`

SET timestamp = TIMESTAMP(DATETIME('2025-04-27', TIME(timestamp))),

logName = 'H_5902_distinct_2025-04-27'

WHERE DATE(timestamp) BETWEEN '2025-04-25' AND '2025-04-28' AND logName NOT IN ('H_5902_distinct_2025-04-25','H_5902_distinct_2025-04-26')

—-------------------------------

Update start time



UPDATE

  `clirnet-dev.request_edit.H_5902_distinct_data`

SET

  jsonPayload.start_time = FORMAT_TIMESTAMP('%Y-%m-%d %H:%M:%S', TIMESTAMP(DATETIME('2025-04-25', TIME(TIMESTAMP(jsonPayload.start_time)))))

WHERE

 logName = 'H_5902_distinct_2025-04-25';



—----------------------------------

Update end time



  UPDATE `clirnet-dev.request_edit.H_5902_distinct_data`

SET jsonPayload.end_time = FORMAT_TIMESTAMP('%Y-%m-%d %H:%M:%S', TIMESTAMP_ADD(TIMESTAMP(jsonPayload.start_time), INTERVAL 5 SECOND))



WHERE logName IN ('H_5902_distinct_2025-04-27','H_5902_distinct_2025-04-26','H_5902_distinct_2025-04-25')





—-----------------------------------

Update timestamp_get



UPDATE `clirnet-dev.request_edit.H_5902_distinct_data`

SET jsonPayload.timestamp_get = UNIX_SECONDS(TIMESTAMP(jsonPayload.start_time))

WHERE logName IN ('H_5902_distinct_2025-04-27','H_5902_distinct_2025-04-26','H_5902_distinct_2025-04-25')

—-----------------------------



Update banner_id



UPDATE `clirnet-dev.request_edit.H_5902_distinct_data`

SET

  jsonPayload.banner_id = '5902'



WHERE 1<>0





—---------------------------------------



Insert to banner table





INSERT INTO `clirnetapp.banner_data.banner_call_data`

SELECT * FROM `clirnet-dev.request_edit.H_5902_distinct_data`



ph1

('H_5902_distinct_2025-04-27','H_5902_distinct_2025-04-26','H_5902_distinct_2025-04-25')



Ph2

('H_5902_distinct_2025-04-28_ph2','H_5902_distinct_2025-04-29_ph2','H_5902_distinct_2025-04-30_ph2')
