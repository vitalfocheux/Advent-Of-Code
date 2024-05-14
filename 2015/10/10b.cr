def look_and_say(sequence)
    sequence.chars.chunk { |char| char }.map { |char, chars| "#{chars.size}#{char}" }.join
  end
  
  sequence = File.read("10.txt").chomp
  50.times { sequence = look_and_say(sequence) }
  
  puts sequence.size