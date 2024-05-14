require "digest"
puts "#{(1..).find { |n| Digest::MD5.hexdigest(File.read("04.txt") + n.to_s).starts_with?("00000") }}"