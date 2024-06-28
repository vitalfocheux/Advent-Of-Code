require 'strscan'

def look_and_say(sequence)
    scanner = StringScanner.new(sequence)
    result = ''

    while !scanner.eos?
        digit = scanner.scan(/(\d)\1*/)
        result << "#{digit.length}#{digit[0]}"
    end

    result
end

def iterate(sequence, iter)
    for i in 1..iter
        sequence = look_and_say(sequence)
    end
    sequence.length
end

input = "1321131112"

puts "#{iterate(input, 40)}"
puts "#{iterate(input, 50)}"