floor = 0
File.read("01.txt").each_char.each_with_index do |c, i|
  c == '(' ? (floor += 1) : (floor -= 1)
  if floor == -1
    puts "#{(i+1)}"
    break
  end
end