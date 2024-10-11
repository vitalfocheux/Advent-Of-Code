import 'dart:io';
import 'package:http/http.dart' as http;

Future<void> fetchAdventInput(int day, int year) async {
  // Remplacez par votre cookie de session
  final String sessionCookie = '_ga=GA1.2.1925324925.1700647242; session=53616c7465645f5f510e80089fb5bbff30fa07b894bd200ddc8735ddc48b9fa4e23c0e947418f3cd9ec71937f2bcd6efab6a30cacf497fdd9dddb578d1d219e1; _ga_MHSNPJKWC7=GS1.2.1727128753.32.1.1727128771.0.0.0; _gid=GA1.2.1195359072.1727726221';
  
  final String url = 'https://adventofcode.com/$year/day/$day/input';
  
  try {
    final response = await http.get(
      Uri.parse(url),
      headers: {
        'Cookie': 'session=$sessionCookie',
        'User-Agent': 'dart-advent-of-code-client',
      },
    );
  
    if (response.statusCode == 200) {
      // Succès : récupérez l'input du problème
      print('Input du jour $day:');
      print(response.body);
    } else {
      // En cas d'erreur
      print('Erreur lors de la récupération des données: ${response.statusCode}');
    }
  } catch (e) {
    print('Une erreur s\'est produite: $e');
  }
}

void main() {
  final int day = 1; // Par exemple, le jour 1
  final int year = 2023; // Par exemple, pour l'année 2023
  
  fetchAdventInput(day, year);
}
