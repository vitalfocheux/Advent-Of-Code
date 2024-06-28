def find_floor(input)
    input.chars.reduce(0) { |floor, char| char == '(' ? floor + 1 : floor - 1 }
end

def find_basement(input)
    input.chars.each_with_index.reduce(0) do |floor, (char, index)|
        return index if floor == -1
        char == '(' ? floor + 1 : floor - 1
    end
end


# Exemple d'utilisation
input = File.read('01.txt')
puts "Le Père Noël se trouve à l'étage #{find_floor(input)}"
puts "Le Père Noël entre dans le sous-sol à la position #{find_basement(input)}"