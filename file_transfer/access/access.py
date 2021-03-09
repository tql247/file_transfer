from file_transfer.config import DATETIME_START, LOCATION, DATETIME_END, TIME_START, TIME_END


def get_video_file_name(connection):
    if not connection:
        return []

    # query db
    cursor = connection.cursor()
    query = f"""
                select file_name, start_point 
                from video_information vi 
                where true
                and file_name like '%{LOCATION}%'
                and vi.start_point::date between date '{DATETIME_START}' and date '{DATETIME_END}'
                and a.start_point::time between time '{TIME_START}' and '{TIME_END}'
                order by vi.start_point asc
            """
    cursor.execute(query)
    record = cursor.fetchall()
    cursor.close()

    # extract location name from file name
    list_video_name = []
    for row in record:
        list_video_name.append(row[0])

    return list_video_name
