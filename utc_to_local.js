#!/usr/local/bin/node
var moment = require('moment-timezone');

function dt_utc_str_to_local(hour) {
  let utc_date = moment(new Date(Date.UTC(2018, 1, 27, hour, 0, 0))).tz('UTC');
  let local_date = moment(utc_date).tz('America/Los_Angeles');
  let utc_str = utc_date.format('ha z');
  let local_str = local_date.format('ha z');

  let suffix = '';
  if(local_date.date() < utc_date.date())
    suffix = 'the previous day';
  else if(local_date.date() > utc_date.date())
    suffix = 'the next day';

  return `${utc_str} == ${local_str} ${suffix}`
}

var hour = process.argv[2];
console.log(dt_utc_str_to_local(hour));
