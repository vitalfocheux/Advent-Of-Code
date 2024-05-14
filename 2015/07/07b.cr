def signal(wires, wire, memo = {} of String => Int32)
  return memo[wire] if memo[wire]?

  if wire.to_i?
    return wire.to_i
  end

  expression = wires[wire]
  result = case expression
           when /(\w+) AND (\w+)/
             signal(wires, $1, memo) & signal(wires, $2, memo)
           when /(\w+) OR (\w+)/
             signal(wires, $1, memo) | signal(wires, $2, memo)
           when /(\w+) LSHIFT (\d+)/
             signal(wires, $1, memo) << $2.to_i
           when /(\w+) RSHIFT (\d+)/
             signal(wires, $1, memo) >> $2.to_i
           when /NOT (\w+)/
             ~signal(wires, $1, memo) & 0xFFFF
           when /\d+/
             expression.to_i
           else
             signal(wires, expression, memo)
           end

  memo[wire] = result
  result
end

wires = {} of String => String
File.read("07.txt").each_line do |line|
  expression, wire = line.split(" -> ")
  wires[wire] = expression
end

signal_a = signal(wires, "a")
new_wires = wires.clone
new_wires["b"] = signal_a.to_s
puts signal(new_wires, "a")