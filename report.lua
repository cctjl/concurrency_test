--
-- 处理 wrk 输出的 lua 脚本
--

done = function(summary, latency, requests)
    io.output(io.stderr)
    duration_sec = summary.duration/1000/1000
    io.write(string.format('  %d requests in %.2fs, %.2fKB read, requests/sec %.2f, transfer/sec %.2fKB\n',
        summary.requests, duration_sec, summary.bytes/1024, summary.requests / duration_sec,
        summary.bytes/1024/duration_sec
    ))
    io.write(string.format('  Socket errors: connect %d, read %d, write %d, status>399 %d, timeout %d\n',
        summary.errors.connect, summary.errors.read, summary.errors.write, summary.errors.status, summary.errors.timeout
    ))
    io.write('\t\tavg\t\tmin\t\tmax\t\tstdev\t\t1%\t\t5%\t\t10%\t\t25%\t\t50%\t\t75%\t\t90%\t\t99%\n')
    io.write('Latency\t\t')
    statLatency(latency)
    io.write('Req/Sec\t\t')
    statRequest(requests)
end

function outStr(str)
    if string.len(str) < 8
    then
        return string.format('%s\t\t', str)
    else
        return string.format('%s\t', str)
    end
end

function statLatency(statObj)
    io.write(outStr(string.format('%.2fms', statObj.mean/1000)))
    io.write(outStr(string.format('%.2fms', statObj.min/1000)))
    io.write(outStr(string.format('%.2fms', statObj.max/1000)))
    io.write(outStr(string.format('%.2fms', statObj.stdev/1000)))
    io.write(outStr(string.format('%.2fms', statObj:percentile(1)/1000)))
    io.write(outStr(string.format('%.2fms', statObj:percentile(5)/1000)))
    io.write(outStr(string.format('%.2fms', statObj:percentile(10)/1000)))
    io.write(outStr(string.format('%.2fms', statObj:percentile(25)/1000)))
    io.write(outStr(string.format('%.2fms', statObj:percentile(50)/1000)))
    io.write(outStr(string.format('%.2fms', statObj:percentile(75)/1000)))
    io.write(outStr(string.format('%.2fms', statObj:percentile(90)/1000)))
    io.write(outStr(string.format('%.2fms', statObj:percentile(99)/1000)))
    io.write('\n')
end

function statRequest(statObj)
    io.write(outStr(string.format('%.2f', statObj.mean)))
    io.write(outStr(string.format('%.2f', statObj.min)))
    io.write(outStr(string.format('%.2f', statObj.max)))
    io.write(outStr(string.format('%.2f', statObj.stdev)))
    io.write(outStr(string.format('%.2f', statObj:percentile(1))))
    io.write(outStr(string.format('%.2f', statObj:percentile(5))))
    io.write(outStr(string.format('%.2f', statObj:percentile(10))))
    io.write(outStr(string.format('%.2f', statObj:percentile(25))))
    io.write(outStr(string.format('%.2f', statObj:percentile(50))))
    io.write(outStr(string.format('%.2f', statObj:percentile(75))))
    io.write(outStr(string.format('%.2f', statObj:percentile(90))))
    io.write(outStr(string.format('%.2f', statObj:percentile(99))))
    io.write('\n')
end