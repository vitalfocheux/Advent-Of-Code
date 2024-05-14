content = File.read("09.txt")

# Analyser l'entrée
distances = Hash(Tuple(String, String), Int32).new
villes = Set(String).new

content.each_line do |line|
  match_data = line.match(/(\w+) to (\w+) = (\d+)/)
  if match_data
    ville1, ville2, distance = match_data[1], match_data[2], match_data[3].to_i
    distances[{ville1, ville2}] = distance
    distances[{ville2, ville1}] = distance
    villes << ville1
    villes << ville2
  end
end

# Générer toutes les permutations des villes
permutations = villes.to_a.permutations

# Calculer la distance totale pour chaque permutation et trouver la plus courte
dist = permutations.map do |permutation|
    permutation.each_cons(2).sum do |pair|
        pair_tuple = {pair[0], pair[1]}
        if distances.has_key?(pair_tuple)
            distances[pair_tuple]
        else
            0
        end
    end
  end.max


puts dist