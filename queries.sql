/* Queries : 
Query 1 : 
1. List all active players playing for GSW
2. How many points has Stephen Curry scored in total ?
3. Which player has the most blocks in his carrer ? 
4. List the names of players who have scored more than 20000 points for their career ?  */

SELECT A.full_name from Active_Players as A where A.id in 
            (SELECT PLAYER_ID from Season_Stats where TEAM_ABBREVIATION = "GSW" );

SELECT  B.full_name, A.PTS from Career_Stats AS A JOIN All_Players as B 
        where B.full_name == "Stephen Curry" and B.id = A.PLAYER_ID;

SELECT  B.full_name, A.BLK from Career_Stats AS A JOIN All_Players as B 
        where B.id = A.PLAYER_ID and A.BLK = (SELECT MAX(BLK) from Career_Stats);
        

SELECT B.full_name, A.PTS from All_Players as B, Career_Stats AS A
        where B.id = A.PLAYER_ID and A.PTS > 20000;
