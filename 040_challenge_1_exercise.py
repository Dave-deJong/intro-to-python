# Video alternative: https://youtu.be/qDWyR0XpJtQ&t=1295s

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words):
  non_hyphened_words = remove_hyphened_words(words)
  long_words = find_long_words(non_hyphened_words)
  shortened_words = shorten_extremely_long_words(long_words)
  display_words = format_display(shortened_words)
  return display_words

def remove_hyphened_words(words):
  for word in words:
    i = 0
    while i < len(word):
      if word[i] == "-":
        i += 1
        words.remove(word)
        break
      else:
        i += 1
  return words

def find_long_words(words):
  long_words = []
  for word in words:
    if len(word) > 10:
      long_words.append(word)
  return long_words

def shorten_extremely_long_words(words):
  shortened_words = []
  for word in words:
    if len(word) <= 15:
      shortened_words.append(word)
    else:
      new_word = word[0:15] + "..."
      shortened_words.append(new_word)
  return shortened_words

def format_display(words):
  display = "These words are quite long: "
  for word in words:
    display += f"{word}, "
  if display[-2] == ",":
    display = display[:-2]
  return display

check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
