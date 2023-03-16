# StorySorter

A program to sort the sentences of a story into alphabetical order.

# Instructions

1. Run "python3 story.py" (or any python3+ interpreter) in your terminal,
   in the same dircetory of this script
2. Then open the newly created "ShortStoryRearranged.txt" file, which will
   be in the same directory as this script, to see the result

# Assumptions

1. The input file is called "ShortStory.txt", is in the same directory
   as this script, and is gramatically correct
2. We are rearranging the sentences in the story into alphabetical order
   by only their first letter
3. The output file will have each sentence on a new line to facilitate easy verification
   that the story has been rearranged correctly into alphabetical order
4. We assume the end of a sentence occurs as follows:
   - First, we verify we are not inside of a quote, as we don't want to
     rearrange sentences inside of a quote, which would cause quotation mark spread everywhere
   - Second, we verify we are not in the middle of a sentence, indicated by a lowercase letter
   - Third, we hit a punctuation ( !, ?, ., : ) or an ending quotation mark
   - Fourth, we then hit a space or newline character
   - Lastly, we hit a capital letter or a starting quotiation mark

# Thought Process

I knew that the algorithm to solve this would need to be at least O(n), since
I'd have to go through each character in the story to find what the sentences are
to rearrange them, so I wanted to make an algorithm that had this minimum complexity.
I thought of efficient ways to store the organized data, and I realized that the sorted
structure is limited to the capital letters of the alphabet. I took advantage of this constraint
and used a dictionary, where the keys are the capital letters of the alphabet, and the values
are the sentences that start with that letter. As such, finding the sentences and sorting them
are both done at the same time through the dictionary. The next step was just figuring out what
constitutes as the end of a sentnece, which I explained in the above section.
