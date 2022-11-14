/* Queries : 
Query 1 : 
/* Queries : 
Query 1 : 
1. How many points has Stephen Curry scored in total ? {input field}
2. List all active players playing for GSW
3. List the names of players who have scored more than 20000 points for their career ? {input field}
4. Which player has the most blocks in his carrer ? 
5. List the names and IDS of players averaging shooting more than <> percent from the field in this season in descending order? {input_field}
 */


SELECT  B.full_name, A.PTS from Career_Stats AS A JOIN All_Players as B 
        where B.full_name == "Stephen Curry" and B.id = A.PLAYER_ID;

SELECT A.full_name from Active_Players as A where A.id in 
            (SELECT PLAYER_ID from Season_Stats where TEAM_ABBREVIATION = "GSW" );

SELECT B.full_name, A.PTS from All_Players as B, Career_Stats AS A
        where B.id = A.PLAYER_ID and A.PTS > 20000;

SELECT  B.full_name, A.BLK from Career_Stats AS A JOIN All_Players as B 
        where B.id = A.PLAYER_ID and A.BLK = (SELECT MAX(BLK) from Career_Stats);

SELECT A.PLAYER_ID, B.full_name, A.FG_PCT from All_Players as B, Season_Stats AS A 
        WHERE (B.id = A.PLAYER_ID and A.FG_PCT > 0.45 and A.SEASON_ID = "2020-21")  ORDER BY A.FG_PCT  DESC ;