require "digest"

content = File.read("04.txt")

nb = 0

while true
  nb += 1
  if Digest::MD5.hexdigest(content + nb.to_s).starts_with?("00000")
    break
  end
end

puts nb