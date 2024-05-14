puts File.read("05.txt").lines.count { |line| line.match(/(..).*\1/) && line.match(/(.).\1/) }
