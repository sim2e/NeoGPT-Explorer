examples = """
# Who is related to King Yeongjo of the Joseon Dynasty?
MATCH (p:Entity WHERE p.id = 'Yeongjo of Joseon' OR p.id = 'Yeongjo')-[:Relationship {type: 'SOCIAL_RELATIONSHIP'}]-(x) RETURN x.id

# When was King Sejong of Joseon Born?
Match(n:Entity WHERE n.id = 'Sejong the Great')-[:RELATIONSHIP {type:'DATE_OF_BIRTH'}]-(x:Entity) return x.id 
        
# Who are sibling of Yangnyeong
Match(n:Entity WHERE n.id = 'Yangnyeong')-[:RELATIONSHIP {type:'SIBLING'}]-(x:Entity) return x.id

# What is nationality of king Jengjo
Match(n:Entity WHERE n.id = 'Jeongjo of Joseon' OR n.id = 'Jengjo')-[:Relationship {type: 'ALL_PERSON_LOCATIONS'}]-(x) RETURN x.id

# When was Sejong Born?
Match(n:Entity WHERE n.id = 'Sejong the Great')-[:RELATIONSHIP {type:'DATE_OF_BIRTH'}]-(x:Entity) return x.id

# What was position of Munjong of Joseon
Match(n:Entity WHERE n.id = 'Munjong of Joseon' OR n.id = 'Munjong')-[:RELATIONSHIP {type: 'POSITION_HELD'}]-(x) RETURN x.id

# Who is parent of Taejong of Joseon
Match(n:Entity WHERE n.id = 'Munjong of Joseon' OR n.id = 'Munjong')-[:RELATIONSHIP {type: 'PARENT'}]-(x) RETURN x.id

# Family member of Taejong of Joseon
Match(n:Entity WHERE n.id = 'Taejong' or n.id = 'Taejong of Joseon')-[:RELATIONSHIP {type: 'FAMILY_MEMBER'}]-(x) RETURN x.id

# When was Taejo born
Match(n:Entity WHERE n.id = 'Taejo' or n.id = 'Taejo of Joseon')-[:RELATIONSHIP {type: 'DATE_OF_BIRTH'}]-(x) RETURN x.id

# When was Taejo died
Match(n:Entity WHERE n.id = 'Taejo' or n.id = 'Taejo of Joseon')-[:RELATIONSHIP {type: 'DATE_OF_DEATH'}]-(x) RETURN x.id

# What was position of Taejo of Joseon
Match(n:Entity WHERE n.id ='Taejo' or n.id = 'Taejo of Joseon')-[:RELATIONSHIP {type: 'POSITION_HELD'}]-(x) RETURN x.id

# What is nationality of Taejo?
Match(n:Entity WHERE n.id = 'Taejo', or n.id = 'Taejo of Joseon')-[:RELATIONSHIP {type: 'ALL_PERSON_LOCATIONS'}]-(x) RETURN x.id
"""
