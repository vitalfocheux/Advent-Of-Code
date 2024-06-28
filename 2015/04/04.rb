
require 'digest/md5'



def md5(zeros)
    number = 0 
    loop do 
        hash = Digest::MD5.hexdigest("iwrupvqb#{number}")
        if hash.start_with?(zeros)
            puts "#{number}"
            break
        end
        number += 1
    end
end

puts "#{md5("00000")}"
puts "#{md5("000000")}"