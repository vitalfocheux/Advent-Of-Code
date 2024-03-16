puts File.read("05.txt").lines.count { |line| !line.match(/ab|cd|pq|xy/) && line.match(/[aeiou].*[aeiou].*[aeiou]/) && line.match(/(.)\1/) }
