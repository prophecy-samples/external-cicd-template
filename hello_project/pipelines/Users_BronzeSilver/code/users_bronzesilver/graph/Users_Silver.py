from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from users_bronzesilver.config.ConfigStore import *
from users_bronzesilver.udfs.UDFs import *

def Users_Silver(spark: SparkSession, in0: DataFrame):
    if spark.catalog._jcatalog.tableExists(f"hello_cicd.{Config.target_table}"):
        from delta.tables import DeltaTable, DeltaMergeBuilder
        existingTable = DeltaTable.forName(spark, f"hello_cicd.{Config.target_table}")
        updatesDF = in0.withColumn("previous", lit("true")).withColumn("current", lit("true"))
        existingDF = existingTable.toDF()
        updateColumns = updatesDF.columns
        stagedUpdatesDF = updatesDF\
                              .join(existingDF, ["id", "env"])\
                              .where(
                                (
                                  (existingDF["current"] == lit("true"))
                                  & (
                                    (
                                      (
                                        (
                                          (
                                            (
                                              (
                                                (
                                                  (
                                                    (
                                                      (
                                                        (
                                                          (
                                                            (
                                                              (
                                                                (
                                                                  (
                                                                    (
                                                                      (
                                                                        (
                                                                          (
                                                                            (
                                                                              (
                                                                                (
                                                                                  (
                                                                                    (
                                                                                      (
                                                                                        (
                                                                                          (
                                                                                            (
                                                                                              (
                                                                                                (
                                                                                                  (
                                                                                                    (
                                                                                                      (
                                                                                                        (
                                                                                                          (
                                                                                                            (
                                                                                                              (
                                                                                                                (
                                                                                                                  (
                                                                                                                    (
                                                                                                                      (
                                                                                                                        (
                                                                                                                          (
                                                                                                                            (
                                                                                                                              existingDF["username"]
                                                                                                                              != updatesDF["username"]
                                                                                                                            )
                                                                                                                            | (
                                                                                                                              existingDF["firstName"]
                                                                                                                              != updatesDF["firstName"]
                                                                                                                            )
                                                                                                                          )
                                                                                                                          | (
                                                                                                                            existingDF["lastName"]
                                                                                                                            != updatesDF["lastName"]
                                                                                                                          )
                                                                                                                        )
                                                                                                                        | (
                                                                                                                          existingDF["age"]
                                                                                                                          != updatesDF["age"]
                                                                                                                        )
                                                                                                                      )
                                                                                                                      | (
                                                                                                                        existingDF["bloodGroup"]
                                                                                                                        != updatesDF["bloodGroup"]
                                                                                                                      )
                                                                                                                    )
                                                                                                                    | (
                                                                                                                      existingDF["birthDate"]
                                                                                                                      != updatesDF["birthDate"]
                                                                                                                    )
                                                                                                                  )
                                                                                                                  | (
                                                                                                                    existingDF["domain"]
                                                                                                                    != updatesDF["domain"]
                                                                                                                  )
                                                                                                                )
                                                                                                                | (
                                                                                                                  existingDF["ein"]
                                                                                                                  != updatesDF["ein"]
                                                                                                                )
                                                                                                              )
                                                                                                              | (
                                                                                                                existingDF["email"]
                                                                                                                != updatesDF["email"]
                                                                                                              )
                                                                                                            )
                                                                                                            | (
                                                                                                              existingDF["eyeColor"]
                                                                                                              != updatesDF["eyeColor"]
                                                                                                            )
                                                                                                          )
                                                                                                          | (
                                                                                                            existingDF["gender"]
                                                                                                            != updatesDF["gender"]
                                                                                                          )
                                                                                                        )
                                                                                                        | (
                                                                                                          existingDF["height"]
                                                                                                          != updatesDF["height"]
                                                                                                        )
                                                                                                      )
                                                                                                      | (
                                                                                                        existingDF["image"]
                                                                                                        != updatesDF["image"]
                                                                                                      )
                                                                                                    )
                                                                                                    | (
                                                                                                      existingDF["ip"]
                                                                                                      != updatesDF["ip"]
                                                                                                    )
                                                                                                  )
                                                                                                  | (
                                                                                                    existingDF["macAddress"]
                                                                                                    != updatesDF["macAddress"]
                                                                                                  )
                                                                                                )
                                                                                                | (
                                                                                                  existingDF["maidenName"]
                                                                                                  != updatesDF["maidenName"]
                                                                                                )
                                                                                              )
                                                                                              | (
                                                                                                existingDF["password"]
                                                                                                != updatesDF["password"]
                                                                                              )
                                                                                            )
                                                                                            | (
                                                                                              existingDF["phone"]
                                                                                              != updatesDF["phone"]
                                                                                            )
                                                                                          )
                                                                                          | (
                                                                                            existingDF["ssn"]
                                                                                            != updatesDF["ssn"]
                                                                                          )
                                                                                        )
                                                                                        | (
                                                                                          existingDF["university"]
                                                                                          != updatesDF["university"]
                                                                                        )
                                                                                      )
                                                                                      | (
                                                                                        existingDF["userAgent"]
                                                                                        != updatesDF["userAgent"]
                                                                                      )
                                                                                    )
                                                                                    | (
                                                                                      existingDF["weight"]
                                                                                      != updatesDF["weight"]
                                                                                    )
                                                                                  )
                                                                                  | (
                                                                                    existingDF["address_city"]
                                                                                    != updatesDF["address_city"]
                                                                                  )
                                                                                )
                                                                                | (
                                                                                  existingDF["address_coordinates_lat"]
                                                                                  != updatesDF["address_coordinates_lat"]
                                                                                )
                                                                              )
                                                                              | (
                                                                                existingDF["address_coordinates_lng"]
                                                                                != updatesDF["address_coordinates_lng"]
                                                                              )
                                                                            )
                                                                            | (
                                                                              existingDF["address_postalCode"]
                                                                              != updatesDF["address_postalCode"]
                                                                            )
                                                                          )
                                                                          | (
                                                                            existingDF["address_state"]
                                                                            != updatesDF["address_state"]
                                                                          )
                                                                        )
                                                                        | (
                                                                          existingDF["address_street"]
                                                                          != updatesDF["address_street"]
                                                                        )
                                                                      )
                                                                      | (
                                                                        existingDF["bank_cardExpire"]
                                                                        != updatesDF["bank_cardExpire"]
                                                                      )
                                                                    )
                                                                    | (
                                                                      existingDF["bank_cardNumber"]
                                                                      != updatesDF["bank_cardNumber"]
                                                                    )
                                                                  )
                                                                  | (
                                                                    existingDF["bank_cardType"]
                                                                    != updatesDF["bank_cardType"]
                                                                  )
                                                                )
                                                                | (
                                                                  existingDF["bank_currency"]
                                                                  != updatesDF["bank_currency"]
                                                                )
                                                              )
                                                              | (
                                                                existingDF["bank_iban"]
                                                                != updatesDF["bank_iban"]
                                                              )
                                                            )
                                                            | (
                                                              existingDF["company_address_street"]
                                                              != updatesDF["company_address_street"]
                                                            )
                                                          )
                                                          | (
                                                            existingDF["company_address_city"]
                                                            != updatesDF["company_address_city"]
                                                          )
                                                        )
                                                        | (
                                                          existingDF["company_address_coordinates_lat"]
                                                          != updatesDF["company_address_coordinates_lat"]
                                                        )
                                                      )
                                                      | (
                                                        existingDF["company_address_coordinates_lng"]
                                                        != updatesDF["company_address_coordinates_lng"]
                                                      )
                                                    )
                                                    | (
                                                      existingDF["company_address_postalCode"]
                                                      != updatesDF["company_address_postalCode"]
                                                    )
                                                  )
                                                  | (
                                                    existingDF["company_address_state"]
                                                    != updatesDF["company_address_state"]
                                                  )
                                                )
                                                | (
                                                  existingDF["company_department"]
                                                  != updatesDF["company_department"]
                                                )
                                              )
                                              | (
                                                existingDF["company_name"]
                                                != updatesDF["company_name"]
                                              )
                                            )
                                            | (
                                              existingDF["company_title"]
                                              != updatesDF["company_title"]
                                            )
                                          )
                                          | (
                                            existingDF["hair_color"]
                                            != updatesDF["hair_color"]
                                          )
                                        )
                                        | (
                                          existingDF["hair_type"]
                                          != updatesDF["hair_type"]
                                        )
                                      )
                                      | (
                                        existingDF["end_time"]
                                        != updatesDF["end_time"]
                                      )
                                    )
                                    | (
                                      existingDF["start_time"]
                                      != updatesDF["start_time"]
                                    )
                                  )
                                )
                              )\
                              .select(*[updatesDF[val] for val in updateColumns])\
                              .withColumn("previous", lit("false"))\
                              .withColumn("mergeKey", lit(None))\
                              .union(updatesDF.withColumn("mergeKey", concat("id", "env")))
        existingTable\
            .alias("existingTable")\
            .merge(
              stagedUpdatesDF.alias("staged_updates"),
              concat(existingDF["id"], existingDF["env"]) == stagedUpdatesDF["mergeKey"]
            )\
            .whenMatchedUpdate(
              condition = (
                (existingDF["current"] == lit("true"))
                & (
                  (
                    (
                      (
                        (
                          (
                            (
                              (
                                (
                                  (
                                    (
                                      (
                                        (
                                          (
                                            (
                                              (
                                                (
                                                  (
                                                    (
                                                      (
                                                        (
                                                          (
                                                            (
                                                              (
                                                                (
                                                                  (
                                                                    (
                                                                      (
                                                                        (
                                                                          (
                                                                            (
                                                                              (
                                                                                (
                                                                                  (
                                                                                    (
                                                                                      (
                                                                                        (
                                                                                          (
                                                                                            (
                                                                                              (
                                                                                                (
                                                                                                  (
                                                                                                    (
                                                                                                      (
                                                                                                        (
                                                                                                          (
                                                                                                            existingDF["username"]
                                                                                                            != stagedUpdatesDF["username"]
                                                                                                          )
                                                                                                          | (
                                                                                                            existingDF["firstName"]
                                                                                                            != stagedUpdatesDF["firstName"]
                                                                                                          )
                                                                                                        )
                                                                                                        | (
                                                                                                          existingDF["lastName"]
                                                                                                          != stagedUpdatesDF["lastName"]
                                                                                                        )
                                                                                                      )
                                                                                                      | (
                                                                                                        existingDF["age"]
                                                                                                        != stagedUpdatesDF["age"]
                                                                                                      )
                                                                                                    )
                                                                                                    | (
                                                                                                      existingDF["bloodGroup"]
                                                                                                      != stagedUpdatesDF["bloodGroup"]
                                                                                                    )
                                                                                                  )
                                                                                                  | (
                                                                                                    existingDF["birthDate"]
                                                                                                    != stagedUpdatesDF["birthDate"]
                                                                                                  )
                                                                                                )
                                                                                                | (
                                                                                                  existingDF["domain"]
                                                                                                  != stagedUpdatesDF["domain"]
                                                                                                )
                                                                                              )
                                                                                              | (
                                                                                                existingDF["ein"]
                                                                                                != stagedUpdatesDF["ein"]
                                                                                              )
                                                                                            )
                                                                                            | (
                                                                                              existingDF["email"]
                                                                                              != stagedUpdatesDF["email"]
                                                                                            )
                                                                                          )
                                                                                          | (
                                                                                            existingDF["eyeColor"]
                                                                                            != stagedUpdatesDF["eyeColor"]
                                                                                          )
                                                                                        )
                                                                                        | (
                                                                                          existingDF["gender"]
                                                                                          != stagedUpdatesDF["gender"]
                                                                                        )
                                                                                      )
                                                                                      | (
                                                                                        existingDF["height"]
                                                                                        != stagedUpdatesDF["height"]
                                                                                      )
                                                                                    )
                                                                                    | (
                                                                                      existingDF["image"]
                                                                                      != stagedUpdatesDF["image"]
                                                                                    )
                                                                                  )
                                                                                  | (
                                                                                    existingDF["ip"]
                                                                                    != stagedUpdatesDF["ip"]
                                                                                  )
                                                                                )
                                                                                | (
                                                                                  existingDF["macAddress"]
                                                                                  != stagedUpdatesDF["macAddress"]
                                                                                )
                                                                              )
                                                                              | (
                                                                                existingDF["maidenName"]
                                                                                != stagedUpdatesDF["maidenName"]
                                                                              )
                                                                            )
                                                                            | (
                                                                              existingDF["password"]
                                                                              != stagedUpdatesDF["password"]
                                                                            )
                                                                          )
                                                                          | (
                                                                            existingDF["phone"]
                                                                            != stagedUpdatesDF["phone"]
                                                                          )
                                                                        )
                                                                        | (
                                                                          existingDF["ssn"]
                                                                          != stagedUpdatesDF["ssn"]
                                                                        )
                                                                      )
                                                                      | (
                                                                        existingDF["university"]
                                                                        != stagedUpdatesDF["university"]
                                                                      )
                                                                    )
                                                                    | (
                                                                      existingDF["userAgent"]
                                                                      != stagedUpdatesDF["userAgent"]
                                                                    )
                                                                  )
                                                                  | (
                                                                    existingDF["weight"]
                                                                    != stagedUpdatesDF["weight"]
                                                                  )
                                                                )
                                                                | (
                                                                  existingDF["address_city"]
                                                                  != stagedUpdatesDF["address_city"]
                                                                )
                                                              )
                                                              | (
                                                                existingDF["address_coordinates_lat"]
                                                                != stagedUpdatesDF["address_coordinates_lat"]
                                                              )
                                                            )
                                                            | (
                                                              existingDF["address_coordinates_lng"]
                                                              != stagedUpdatesDF["address_coordinates_lng"]
                                                            )
                                                          )
                                                          | (
                                                            existingDF["address_postalCode"]
                                                            != stagedUpdatesDF["address_postalCode"]
                                                          )
                                                        )
                                                        | (
                                                          existingDF["address_state"]
                                                          != stagedUpdatesDF["address_state"]
                                                        )
                                                      )
                                                      | (
                                                        existingDF["address_street"]
                                                        != stagedUpdatesDF["address_street"]
                                                      )
                                                    )
                                                    | (
                                                      existingDF["bank_cardExpire"]
                                                      != stagedUpdatesDF["bank_cardExpire"]
                                                    )
                                                  )
                                                  | (
                                                    existingDF["bank_cardNumber"]
                                                    != stagedUpdatesDF["bank_cardNumber"]
                                                  )
                                                )
                                                | (
                                                  existingDF["bank_cardType"]
                                                  != stagedUpdatesDF["bank_cardType"]
                                                )
                                              )
                                              | (
                                                existingDF["bank_currency"]
                                                != stagedUpdatesDF["bank_currency"]
                                              )
                                            )
                                            | (
                                              existingDF["bank_iban"]
                                              != stagedUpdatesDF["bank_iban"]
                                            )
                                          )
                                          | (
                                            existingDF["company_address_street"]
                                            != stagedUpdatesDF["company_address_street"]
                                          )
                                        )
                                        | (
                                          existingDF["company_address_city"]
                                          != stagedUpdatesDF["company_address_city"]
                                        )
                                      )
                                      | (
                                        existingDF["company_address_coordinates_lat"]
                                        != stagedUpdatesDF["company_address_coordinates_lat"]
                                      )
                                    )
                                    | (
                                      existingDF["company_address_coordinates_lng"]
                                      != stagedUpdatesDF["company_address_coordinates_lng"]
                                    )
                                  )
                                  | (
                                    existingDF["company_address_postalCode"]
                                    != stagedUpdatesDF["company_address_postalCode"]
                                  )
                                )
                                | (
                                  existingDF["company_address_state"]
                                  != stagedUpdatesDF["company_address_state"]
                                )
                              )
                              | (
                                existingDF["company_department"]
                                != stagedUpdatesDF["company_department"]
                              )
                            )
                            | (
                              existingDF["company_name"]
                              != stagedUpdatesDF["company_name"]
                            )
                          )
                          | (existingDF["company_title"] != stagedUpdatesDF["company_title"])
                        )
                        | (existingDF["hair_color"] != stagedUpdatesDF["hair_color"])
                      )
                      | (existingDF["hair_type"] != stagedUpdatesDF["hair_type"])
                    )
                    | (existingDF["end_time"] != stagedUpdatesDF["end_time"])
                  )
                  | (existingDF["start_time"] != stagedUpdatesDF["start_time"])
                )
              ),
              set = {
"current" : "false", "end_time" : "staged_updates.start_time"}
            )\
            .whenNotMatchedInsertAll()\
            .execute()
    else:
        in0.write\
            .format("delta")\
            .option("path", f"dbfs:/FileStore/Prophecy/hello_cicd/{Config.env}/bronze/users")\
            .mode("overwrite")\
            .saveAsTable(f"hello_cicd.{Config.target_table}")
