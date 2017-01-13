import unittest
# import re
import spacy
nlp = spacy.load('en')

#WE ARE WORKING WITH THE FOLLOWING LIST in most of the functions below:
#[('There', '', 'expl', 'ADV'), ('was', '', 'ROOT', 'VERB'), ('also', '', 'advmod', 'ADV'), ('a', '', 'det', 'DET'), ('death', '', 'attr', 'NOUN'), ('in', '', 'prep', 'ADP'), ('neighboring', '', 'amod', 'VERB'), ('Vermont', 'GPE', 'pobj', 'PROPN'), ('.', '', 'punct', 'PUNCT')]
def pos_tup_list(s):
    processed = nlp(s)
    tup_list = []
    for token in processed:
        tup_list.append((str(token),token.ent_type_,token.dep_,token.pos_))
    return tup_list

def consec_iden_pos(lst):
    for index in range(len(lst)):
        iden_tup = lst[index][3]
        if iden_tup == 'NOUN' or iden_tup == 'PRON' or iden_tup == 'PROPN':
            consec_lst = [index]
            for i in range(index + 1, len(lst)):
                next_iden_found = lst[i][3]
                next_next_iden = lst[i+1][3]
                if lst[i][0] == '.' and (next_next_iden == 'NOUN' or next_next_iden == 'PRON' or next_next_iden == 'PROPN'):
                    consec_lst.append(i)
                elif next_iden_found == 'NOUN' or next_iden_found == 'PRON' or next_iden_found == 'PROPN':
                    consec_lst.append(i)
                else:
                    return consec_lst
    return []

def delete_arr_elements(sent_lst,remove_lst):
    new_sent_list = []
    for i in range(len(sent_lst)):
        if i not in remove_lst:
            new_sent_list.append(sent_lst[i])
    return new_sent_list

def capitalize_begin_sent(word):
    new_s = ''
    if word[0].islower():
        new_s += word[0].upper() + word[1:]
    else:
        new_s += word
    return new_s

def make_str(lst):
    s = ''
    if lst[0][3] == 'PUNCT':
        s += capitalize_begin_sent(lst[1][0])
        start_ind = 2
    else:
        s+= capitalize_begin_sent(lst[0][0])
        start_ind = 1
    for i in range(start_ind,len(lst)):
        curr_word = lst[i][0]
        if lst[i][3] != 'PUNCT' and lst[i][2] != "case":
            s += ' ' + curr_word
        else:
            s += curr_word
    return s

def print_tup_removed(lst,rem_lst):
    tups_rem = ''
    for i in range(len(lst)):
        if i in rem_lst:
            tups_rem += str(lst[i]) + ' '
    return tups_rem

def noun_removal(s):
    orig_sent_arr = pos_tup_list(s)
    consec_pos = consec_iden_pos(orig_sent_arr)
    if consec_pos != []:
        upd_sent_arr = delete_arr_elements(orig_sent_arr, consec_pos)
        return (make_str(upd_sent_arr).rstrip('\n'), print_tup_removed(orig_sent_arr, consec_pos).rstrip('\n'))
    else:
        return ("ERROR",None)

def verb_removal(s):
    verb_index = -1
    tup_sent_arr = pos_tup_list(s)
    for i in range(len(tup_sent_arr)):
        if tup_sent_arr[i][3] == "VERB":
            verb_index = i
            verb_found_tup = tup_sent_arr[i]
            break
    if verb_index != -1:
        del tup_sent_arr[verb_index]
        return (make_str(tup_sent_arr).rstrip('\n'), str(verb_found_tup).rstrip('\n'))

    else:
        return ("ERROR",None)


# with open('./updatedSentences/nounCompleteSentences.txt','w') as complete:
#     with open('./updatedSentences/nounRemovedSentences.txt','w') as remov:
#         with open('./originalSentences/nounScreening.txt','r') as file:
#             for line in file:
#                 complete.write(line)
#                 n_sentence_rem = noun_removal(line)  ##make sure this works for ERROR
#                 if n_sentence_rem[0] != "ERROR":
#                     remov.write(n_sentence_rem[0] + ' ||| ' +  n_sentence_rem[1] + ' ||| ' + line)
#                 else:
#                     remov.write("ERROR" + ' ||| ' + line)
#
# with open('./updatedSentences/verbCompleteSentences.txt','w') as v_complete:
#     with open('./updatedSentences/verbRemovedSentences.txt','w') as v_remov:
#         with open('./originalSentences/verbScreening.txt','r') as f:
#             for line in f:
#                 v_complete.write(line)
#                 v_sentence_rem = verb_removal(line)
#                 if v_sentence_rem[0] != "ERROR":
#                     v_remov.write(v_sentence_rem[0] + ' ||| ' +  v_sentence_rem[1] + ' ||| ' + line)
#                 else:
#                     v_remov.write("ERROR" + ' ||| ' + line)

#MAKE THIS FASTER TO RUN!!!
with open('./updatedSentences/nounverbCompleteSentences.txt','w') as nv_complete:
    with open('./updatedSentences/nounverbRemovedSentences.txt','w') as nv_remov:
        with open('./originalSentences/nounverbScreening.txt','r') as fi:
            for line in fi:
                nv_complete.write(line)
                noun_removed = noun_removal(line)
                if noun_removed[0] == "ERROR":
                    nv_remov.write("ERROR" + ' ||| ' + line)
                else:
                    verb_removed = verb_removal(noun_removed[0]) # check if there is an error in verb as well
                    if verb_removed[0] != "ERROR":
                        nv_remov.write(verb_removed[0] + ' ||| ' + noun_removed[1] + verb_removed[1] + ' ||| ' + line) ###THERE IS A PROBLEM HERE CHECK FOR POSIBLE ERROR
                    else:
                        nv_remov.write("ERROR" + ' ||| ' + line)


#next step is to remove verbs, make sure to commit the code you wrote above! before writing for verbs
#determine whether to remove ent, dep, pos

#####CHECK:
# The uncommented code includes my tests and also previous functions I wrote to check word entity and word dependencies
# class removing_nouns(unittest.TestCase):
#     def test(self):
#         self.assertEqual(noun_removal('Washington is my favorite place.'), 'Is my favorite place.')
#         self.assertEqual(noun_removal("Lt. Colonel Seth Reed and his family moved to the Erie area from Geneva, New York; they were Yankees from Uxbridge, Massachusetts."), "And his family moved to the Erie area from Geneva, New York; they were Yankees from Uxbridge, Massachusetts.")
#         self.assertEqual(noun_removal('I saw Catherine Yesenia and Karen walk the dog.'), 'Saw Catherine Yesenia and Karen walk the dog.')
#         self.assertEqual(noun_removal('The cat loves pie.'), 'The loves pie.')
#         self.assertEqual(noun_removal('Kerry and Nando went hiking.'), 'And Nando went hiking.')
#         self.assertEqual(noun_removal('There are also research facilities operated through hospitals and private biotechnology companies.'), "There are also operated through hospitals and private biotechnology companies.")
#         self.assertEqual(noun_removal('He likes to eat.'), 'Likes to eat.')
#         self.assertEqual(noun_removal('Grand Teton National Park and the surrounding region host over 1000 species of vascular plants.'), 'And the surrounding region host over 1000 species of vascular plants.')
#         self.assertEqual(noun_removal('Of the primary schools, there are 162 regular, 14 special, 15 art, and 4 adult schools.'), 'Of the primary, there are 162 regular, 14 special, 15 art, and 4 adult schools.')
#         self.assertEqual(noun_removal('There is no extant literature in the English language in this era.'), 'There is no extant in the English language in this era.')
#         self.assertEqual(noun_removal("This fact, too, was widely criticized by the state's newspapers."), "This, too, was widely criticized by the state's newspapers.")
#         self.assertEqual(noun_removal("Within Black Moshannon State Park there is a State Park Natural Area protecting the bogs."), "Within there is a State Park Natural Area protecting the bogs.")
#         self.assertEqual(noun_removal("C Squadron, leading a brigade group, advanced towards Gambut on the morning of 23 November."), "Leading a brigade group, advanced towards Gambut on the morning of 23 November.")
#         self.assertEqual(noun_removal("Let's go see the cake tree."), "Let go see the cake tree.") #but the output sentence is incorrect
#         self.assertEqual(noun_removal("There was also a death in neighboring Vermont."), "There was also a in neighboring Vermont.") #but the output sentence is incorrect
#
# if __name__ == '__main__':
#     unittest.main()

# def consec_iden_ent_pos(lst,tup_index,f_check,s_check,t_check):
#     for index in range(len(lst)):
#         iden_tup = lst[index][tup_index]
#         if iden_tup == f_check or iden_tup == s_check or iden_tup == t_check: #should i break somewhere here??
#             consec_lst = [index]
#             for i in range(index + 1, len(lst)):
#                 next_iden_found = lst[i][tup_index]
#                 if next_iden_found == f_check or next_iden_found == s_check or next_iden_found == t_check:
#                     consec_lst.append(i)
#                 else:
#                     return consec_lst
#     return []

# def dep_consec_iden(lst):
#     reg = re.compile('.subj')
#     for i in range(len(lst)):
#         dep_tup = lst[i][2]
#         reg_m = reg.match(dep_tup)
#         if reg_m != None:
#             return i
#     return -1

# def ent_noun_removal(s):
#     processed = nlp(s)
#     orig_sent_arr = []
#     for token in processed:
#         orig_sent_arr.append((str(token),token.ent_type_,token.dep_,token.pos_))
#     consec_ent = consec_iden_ent_pos(orig_sent_arr,1,'PERSON','FACILITY','ORG')
#     if consec_ent != []:
#         upd_sent_arr = delete_arr_elements(orig_sent_arr, consec_ent)
#         return make_str(upd_sent_arr)
#     else:
#         consec_dep = dep_consec_iden(orig_sent_arr)
#         if consec_dep != -1:
#             del orig_sent_arr[consec_dep]
#             return make_str(orig_sent_arr)
#         else:
#             consec_pos = consec_iden_ent_pos(orig_sent_arr,3,'NOUN','PRON','PROPN')
#             if consec_pos != []:
#                 upd_sent_arr = delete_arr_elements(orig_sent_arr, consec_pos)
#                 return make_str(upd_sent_arr)
#             else:
#                 return "Sorry I can't check for this."
