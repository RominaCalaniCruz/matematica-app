import random
import math
import sympy as sp

#VARIABLES GLOBALES
message = "Se acerca el fin del mundo 12/12"
coefficient = random.randint(1,10)
independent_variable = random.randint(1,10)
maximun_lives = 10
current_lives = maximun_lives
current_level = 1



def start_game(encryp_message):
  global current_lives, current_level

  while current_lives > 0 and current_level <= 5:
    print(f"Nivel {current_level} - Vidas restantes: {current_lives}")
    isAnswerCorrect = determinate_truth_value_level()

    if isAnswerCorrect:
      print("¡Lo hiciste bien! Pasas al siguinete nivel")
      current_level += 1

    # else:
      # print(f"Respuesta incorrecta. Te quedan {current_lives} vidas.")

  if current_level > 5:
    print("¡Felicidades! Has completado todos los niveles.")
    print_encryp_message(encryp_message)
    decrypted_message = decryp_words(encryp_message)
    print(f"Mensaje desencriptado: {decrypted_message}")

  elif current_lives == 0:
    print("¡Game Over! Te quedaste sin vidas.")

#IMPRIMIR LAS NUMEROS DEL MENSAJE ENCRIPTADO
def print_encryp_message(encryp_message):
  encryp_message_string = ""

  for i in range(len(encryp_message)):
    if i < len(encryp_message) - 1:
      encryp_message_string += str(encryp_message[i]) + "-"
    else:
      encryp_message_string += str(encryp_message[i])

  print("El mensaje encriptado es: "+ encryp_message_string)

# DETERMINAR SI EL JUGADOR RESPONDE BIEN LAS PREGUNTAS DEL NIVEL
def determinate_truth_value_level():
  global current_level

  if current_level == 1:
    boolean_value_level = induction_level()
  elif current_level == 2:
    boolean_value_level = sets_level()
  elif current_level == 3:
    boolean_value_level = relations_level()
  elif current_level == 4:
    boolean_value_level = idk_level()
  elif current_level == 5:
    boolean_value_level = functions_level()
  else:
    boolean_value_level = False

  return boolean_value_level

#CIFRAR EL MENSAJE
def encryp_words(original_message):
  global coefficient, independent_variable

  letter_position = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,  'ñ': 27
  }
  encryp_message = []
  lowercase_message = original_message.lower()

  for letter in lowercase_message:
    if letter in letter_position:
      current_letter_position = letter_position[letter]
      encryp_function = (coefficient * current_letter_position) + independent_variable
      encryp_message.append(encryp_function)

    else:
      encryp_message.append(letter)

  return encryp_message

#DESENCRIPTAR EL MENSAJE
def decryp_words(encryp_message):
  global independent_variable, coefficient

  letter_position_reversed = {
      1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
      11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's',
      20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: 'ñ'
  }
  decrypted_message = ""

  for value in encryp_message:
    if type(value) == int:
      inverse_function = (value - independent_variable)// coefficient

      if inverse_function in letter_position_reversed:
        decrypted_message += letter_position_reversed[inverse_function]
      else:
        decrypted_message += '?'
    else:
      decrypted_message += value

  return decrypted_message



#NIVEL - 1 - Gabriel Mamani ----------------------------------------------------------------------------------------------------------------
def induction_level():
    global current_lives
    print("Nivel 1: Inducción Matemática")
    answer = False
    questions = {
        1: ("1 + 2 + 3....+n = n(n+1)/2", False),
        2: ("1^2 + 2^2 + 3^2....+n^2 = n(n+1)(2n+1)/6", True),
        3: ("1^3 + 2^3 + 3^3....+n^3 = [n(n+1)/2]^2", False),
        4: ("1 * 2 + 2 * 3 + 3 * 4 +....+ n(n+1) = n(n+1)(n+2)/3", True),
        5: ("1 * 2 * 3 + 2 * 3 * 4 +....+ n(n+1)(n+2) = n(n+1)(n+2)(n+3)/3", False),
        6: ("1 + 3 + 5....+ (2n -1) = n^2", True),
        7: ("2^3 + 4^3 + 6^3 +....+ (2n)^3 = (2n)^2 * [(n+1)^2]", False),
        8: ("1/1*2*3 + 1/2*3*4 +....+1/n(n+1)(n+2) = n(n +3)/4(n+1)(n+2)", True),
        9: ("1^3 + 3^3 + 5^3 +....+ (2n-3)^2 + (2n -1)^2 = n^2 * (2n^2 -1)", False),
        10: ("1/1*2 + 1/2*3 +....+1/n(n+1) = n(n +3)/4(n+1)(n+2)", True)
    }
    question_num = random.randint(1,len(questions))
    question_text, correct_answer = questions[question_num]
    
    print("Verifique con el princípio de inducción si la siguiente afirmación es verdadera o falsa")
    print("True = 1\nFalse = 0")
    print(question_text)
    while current_lives > 0:
        try:
            user_answer = int(input("Respuesta: "))
            if user_answer == int(correct_answer):
                print("¡Correcto!")
                answer = True
                break
            current_lives -= 1
            if current_lives > 0:
                print(f"Incorrecto. Te quedan {current_lives} vidas. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa 1 para True o 0 para False.")
  
    return answer
  


#Nivel - 2 - Alejandra ----------------------------------------------------------------------------------------------------------------
def ask_operation(operation, correct_result):
  is_correct = False
  print(f"¿Cuál es el resultado de {operation}?")
  print("------->" , correct_result)

  while True:
        user_input = input("Introduce tu respuesta (ejemplo: 1,2,3)(si es un conjunto vacío coloca 0): ")
        
        try:
            if user_input == "0":
                user_answer = set()
            else:
                user_answer = set(map(int, user_input.split(',')))
            
            if user_answer == correct_result:
                print("¡Respuesta correcta!")
                is_correct = True
                break
            else:
                print("Respuesta incorrecta. Inténtalo de nuevo.")
                global current_lives
                current_lives -= 1
                print(f"Te quedan {current_lives} vidas.")
                if current_lives <= 0:
                    print("No te quedan vidas. Fin del juego.")
                    break
        except ValueError:
            print("Entrada inválida.")
    
  return is_correct

# NIVEL 2 - OPERACIONES DE CONJUNTOS
def sets_level():
  global current_lives
  isCorrect= True

  size_set_a = random.randint(4, 7)
  size_set_b = random.randint(4, 7)

  set_a = random.sample(range(1, 9), size_set_a)
  set_b = random.sample(range(1, 9), size_set_b)
  set_a = set(set_a)
  set_b = set(set_b)

  print(f"Conjunto A = {set_a}, y su cardinalidad es |A| = {size_set_a}")
  print(f"Conjunto B = {set_b}, y su cardinalidad es |B| = {size_set_b}")

  operation_results = {
    'union': set_a | set_b,
    'intersection': set_a & set_b,
    'difference_ab': set_a - set_b,
    'difference_ba': set_b - set_a,
    'symmetric_difference': set_a.symmetric_difference(set_b)
  }

  for operation, correct_result in operation_results.items():
    if not ask_operation(operation, correct_result):
        isCorrect = False
        break

  return isCorrect

#Nivel - 3 - Gabriel Guaman ----------------------------------------------------------------------------------------------------------------

#generar la relacion aleatoria
def random_relation(elements):
    possible_pairs = [(a, b) for a in elements for b in elements]
    num_pairs = random.randint(1, len(possible_pairs))
    return random.sample(possible_pairs, num_pairs)

def format_relation(relation):
    return "{" + ", ".join(f"({a}, {b})" for a, b in relation) + "}"

#verificar si la relacion es reflexiva simetrica antisimetrica y transitiva
def reflexive_rule(relation, elements):
    for x in elements:
        if (x, x) not in relation:
            return False
    return True

def symetric_rule(relation):
    for (a, b) in relation:
        if (b, a) not in relation:
            return False
    return True

def antisymmetric_rule(relation):
    for (a, b) in relation:
        if a != b and (b, a) in relation:
            return False
    return True

def transitive_rule(relation):
    for (a, b) in relation:
        for (c, d) in relation:
            if b == c and (a, d) not in relation:
                return False
    return True

def relations_level():
    global current_lives

    elements = [1, 2, 3, 4]
    relation = random_relation(elements)
    sorted_relation = sorted(relation)
    result = False

    print("Bienvenid@ al nivel 3")
    print("Adivina la relacion correcta")
    print(f"\nRelación  (N={len(relation)}): {format_relation(sorted_relation)}")
    
    correct_answers = {
        "Reflexiva": reflexive_rule(relation, elements),
        "Simétrica": symetric_rule(relation),
        "Antisimétrica": antisymmetric_rule(relation),
        "Transitiva": transitive_rule(relation)
    }

    correct_count = 0
    for property_name, correct_value in correct_answers.items():
        while current_lives > 0:
            user_input = input(f"¿Es {property_name.lower()}? (Sí/No): ").strip().lower()

            if user_input not in ["sí", "s", "y", "yes", "1", "si", "no", "n", "0"]:
                print("Entrada inválida. Ingresa Si/No")
                continue
            
            user_answer = user_input in ["sí", "s", "y", "yes", "1", "si"]

            if user_answer == correct_value:
                print("CORRECTO")
                correct_count += 1
                break
            else:
                current_lives -= 1
                print(f"INCORRECTO.\nTe quedan {current_lives} vidas.")
                # if current_lives <= 0:
                #   print("Se te acabaron los intento.")
                #   break
    if correct_count == 4:         
      print("Felicidades acertaste en todas puedes pasar al siguiente nivel")
    return result

#Nivel 4 - Florencia ----------------------------------------------------------------------------------------------------------------
def generate_set():
    return set(random.sample(range(1, 31), 14))  # Genera un conjunto de 14 elementos aleatorios entre 1 y 30

def generate_relation(A):
    X = random.randint(2, 10)  # Número aleatorio X para la relación
    R = {(x, y) for x in A for y in A if x % X == 0 and y % X == 0}  # Relación basada en múltiplos de X num random
    return A, X, R

def idk_level():
    global current_lives

    print("Nivel 4: Relaciones")
    A, X, R = generate_relation(generate_set())

    print(f"Conjunto A: {A}")
    print(f"Número aleatorio para la relación MCM = {X}")
    print(f"Determina qué pares (x, y) pertenecen a la relación si: R = {{(x,y) | x,y ∈ A son multiplos de {X}}}")

    result = False
    while current_lives > 0:
        user_input = input("Introduce los pares en formato (x,y);(a,b);... o 0 para vacío: ").strip()

        try:
            if user_input == "0":
                user_answer = set()
            else:
                user_answer = set(
                    tuple(map(int, pair.strip().strip('()').split(',')))
                    for pair in user_input.split(';')
                )
        except ValueError:
            print("Entrada inválida.")
            continue

        if user_answer == R:
            print("¡Correcto!")
            result = True
            break
        else:
            current_lives -= 1
            print(f"Respuesta incorrecta. Te quedan {current_lives} vidas.")
            if current_lives == 0:
                print(f"Se te acabaron las vidas. La relación correcta era: {R}")

    return result

#Nivel - 5 - Romina ----------------------------------------------------------------------------------------------------------------

def functions_level():
    global current_lives
    final_response = False
    types_functions = ["lineal", "logaritmica","exponencial","cuadratica"]
    rand_type = random.randint(0, len(types_functions)-1)
    function_to_evaluated = types_functions[rand_type]
    #x = sp.Symbol('x')
   # funcion = -7 * x -1
    function_value = generate_function(function_to_evaluated)
    print("-----respuesta-----")
    print(is_injective(function_value))
    print(is_surjective(function_value))
    print("----------")
    print("\nNivel 5: Clasificacion de funciones.")
    print("\nAnalice la siguiente funcion y elija una opcion...")
    print(f"f(x): {print_function(function_value)}")

    correct_answer = (
        "1" if is_injective(function_value) and not is_surjective(function_value) else
        "2" if is_surjective(function_value) and not is_injective(function_value) else
        "3" if is_injective(function_value) and is_surjective(function_value) else
        "4"
    )

    while current_lives > 0:
        usuario_resp = input("\n [1]: Inyectiva \n [2]: Sobreyectiva \n [3]: Biyectiva \n [4]: Ninguna\n")

        if usuario_resp in ["1", "2", "3", "4"]:
            if usuario_resp == correct_answer:
                print("¡CORRECTO!")
                final_response = True
                break
            else:
                current_lives -= 1
                print(f"INCORRECTO. Te quedan {current_lives} vidas.")
        else:
            print("Entrada inválida.")


    return final_response


def generate_function(type_function):
    x = sp.Symbol('x')
    if type_function == "lineal":
      a, b = random.randint(-10, 10), random.randint(-10, 10)
      function_value = a * x + b

    elif type_function == "cuadratica":
      a, b, c = random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)
      function_value = a * x**2 + b * x + c

    elif type_function == "logaritmica":
      base = random.choice([sp.E, 10])
      function_value = sp.log(x, base)

    elif type_function == "exponencial":
      a, b, c = random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)
      base = random.choice([sp.E, random.randint(2, 10)])
      function_value = base ** x + a

    return function_value

def is_injective(function_value):
  x = sp.Symbol('x')
  derivative = sp.diff(function_value, x)
  derivative_sign = sp.simplify(sp.sign(derivative))

  if derivative_sign == 1 or derivative_sign == -1:
    result = True
  elif function_value.has(x**2):
    result = False
  elif function_value.has(sp.log):
    result = True
  elif function_value.has(sp.exp) or any(function_value.has(a**x) for a in range(2, 11)):
    result = True

  return result


def is_surjective(function_value):
    x = sp.Symbol('x')
    lower_limit = sp.limit(function_value, x, -sp.oo)
    upper_limit = sp.limit(function_value, x, sp.oo)

    if function_value.is_polynomial() and sp.degree(function_value) == 1:
        return True

    if function_value.has(sp.log):
        return False

    if function_value.has(sp.exp):
        return False

    return lower_limit == -sp.oo and upper_limit == sp.oo

def print_function(function_value):
  if 'exp' in str(function_value):
    result = str(function_value).replace("exp(x)", "e^x")
  else:
    function_str = str(function_value).replace("**", "^")
    result = str(function_str).replace("*", "")
  return result


#MAIN
def main():
    encryp_message = encryp_words(message)
    start_game(encryp_message)

#LLAMADA AL MAIN
if __name__ == "__main__":
    main()