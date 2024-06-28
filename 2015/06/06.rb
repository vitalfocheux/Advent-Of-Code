# Initialiser la grille de lumières
grid = Array.new(1000) { Array.new(1000, false) }

def parse_instruction(instruction)
    if instruction.start_with?("turn on")
        action = :turn_on
    elsif instruction.start_with?("turn off")
        action = :turn_off
    elsif instruction.start_with?("toggle")
        action = :toggle
    end
    
    coords = instruction.scan(/\d+,\d+/).map { |pair| pair.split(",").map(&:to_i) }
    [action, coords[0][0], coords[0][1], coords[1][0], coords[1][1]]
end

# Lire les instructions
instructions = File.read("06.txt").split("\n")

# Appliquer les instructions
instructions.each do |instruction|
    # Extraire l'action et les coordonnées de l'instruction
    action, x1, y1, x2, y2 = parse_instruction(instruction)
    
    # Appliquer l'action à la grille
    (x1..x2).each do |x|
        (y1..y2).each do |y|
            case action
            when :turn_on
                grid[x][y] = true
            when :turn_off
                grid[x][y] = false
            when :toggle
                grid[x][y] = !grid[x][y]
            end
        end
    end
end

# Compter le nombre de lumières allumées
lights_on = grid.flatten.count(true)
puts lights_on

# Initialiser la grille d'intensité des lumières
grid = Array.new(1000) { Array.new(1000, 0) }

# Lire les instructions
instructions = File.read("06.txt").split("\n")

# Appliquer les instructions
instructions.each do |instruction|
    # Extraire l'action et les coordonnées de l'instruction
    action, x1, y1, x2, y2 = parse_instruction(instruction)
    
    # Appliquer l'action à la grille
    (x1..x2).each do |x|
        (y1..y2).each do |y|
            case action
            when :turn_on
                grid[x][y] += 1
            when :turn_off
                grid[x][y] = [0, grid[x][y] - 1].max
            when :toggle
                grid[x][y] += 2
            end
        end
    end
end

# Compter l'intensité totale des lumières
total_brightness = grid.flatten.sum
puts total_brightness