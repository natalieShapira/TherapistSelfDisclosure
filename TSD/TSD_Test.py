
class TSD_Test(object):
    TSD_DEFINITION = """
Below are definitions of two subcategories of  Self-disclosure and of not a  self-disclosure:

Non-immediate TSD: Self-disclosure of information about the therapist
* Relates to disclosing, during a treatment session, facts about the therapists’ life outside of the treatment and personal insights they gained, the way they reached these insights, effective / in-effective ways of coping based on their experience and the way they formulated them, emotions that they experience in different situations in their life, etc…
* Example: 
Speech turn: I remember going through a career change a few years ago, and it was a challenging time for me. It's normal to feel uncertain during transitions, but it's also a chance to explore new possibilities.
Answer: Non-immediate TSD

Immediate TSD: Self-disclosure that relates to the "here and now"
* Relates to sharing therapists’ feelings, associations, and thoughts relating to the client and the issues and topics raised during the session and of their emotions, feelings, and thoughts on the therapy process which they are both part of, etc…
* Example: 
Speech turn: I was genuinely excited to hear about the progress you've made.
Answer: Immediate TSD

Not a TSD: Not a Self-disclosure
* Any comment or other therapeutic intervention (e.g., interpretation, clarification, confrontation, reflection, etc.) that does not include therapist self-disclosure.
* Example: 
Speech turn: You say you love your family
Answer: Not a TSD (clarification)
    """

    INSTRUCTION = "\nFor the next speech turn, determine whether it is non-immediate TSD or immediate TSD according to the above definitions. \nSpeech turn: "
    MODEL_TEST_PROMPT_PREFIX = "TEST:\n" + TSD_DEFINITION + INSTRUCTION

#print(MODEL_TEST_PROMPT_PREFIX)



