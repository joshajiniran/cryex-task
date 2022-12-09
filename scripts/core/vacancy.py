import logging
from grpc._channel import _InactiveRpcError
from  grpc import RpcError

import faker
from locust import SequentialTaskSet, task

from protobufs import vacancy_service_pb2

logger = logging.getLogger(__name__)

fake = faker.Faker()


class UserVacancyTaskSet(SequentialTaskSet):
    vacancy_id: str = ""

    @task
    def create_vacancy(self):
        try:
            vacancy_request = (
                vacancy_service_pb2.rpc__create__vacancy__pb2.CreateVacancyRequest(
                    Title=fake.job(),
                    Description=fake.sentence(nb_words=50),
                    Division=fake.random_int(min=0, max=3),
                    Country=fake.country(),
                )
            )
            response = self.client.CreateVacancy(vacancy_request)
            self.vacancy_id = response.vacancy.Id
            logger.info(f"Created vacancy {self.vacancy_id}")
        except AttributeError as e:
            logger.info(f"Error occurred while creating vacancy: {e.args}")
        except RpcError as e:
            logger.info(f"Error occured on server: {e} {e.args}", exc_info=1)

    @task
    def update_vacancy(self):
        try:
            vacancy_update_request = (
                vacancy_service_pb2.rpc__update__vacancy__pb2.UpdateVacancyRequest(
                    Id=self.vacancy_id,
                    Description=fake.sentence(nb_words=50),
                    Division=fake.random_int(min=0, max=3),
                )
            )
            response = self.client.UpdateVacancy(vacancy_update_request)
            logger.info(f"Updated vacancy {response.vacancy}")
        except AttributeError as e:
            logger.info(f"Error occurred and could not update vacancy: {e.args}")
        except RpcError as e:
            logger.info(f"Error occured on server: {e} {e.args}", exc_info=1)

    @task
    def fetch_vacancy(self):
        try:
            response = self.client.GetVacancy(
                vacancy_service_pb2.VacancyRequest(Id=self.vacancy_id)
            )
            logger.info(f"Fetched vacancy {response.vacancy}")
        except AttributeError as e:
            logger.info(f"Error occurred while fetching vacancy: {e.args}")
        except RpcError as e:
            logger.info(f"Error occured on server: {e} {e.args}", exc_info=1)

    @task
    def delete_vacancy(self):
        try:
            self.client.DeleteVacancy(
                vacancy_service_pb2.VacancyRequest(Id=self.vacancy_id)
            )
            logger.info(f"Deleted vacancy {self.vacancy_id}")
        except AttributeError as e:
            logger.info(f"Error occurred and could not delete vacancy: {e.args}")
        except RpcError as e:
            logger.info(f"Error occured on server: {e} {e.args}", exc_info=1)

    @task
    def stop(self):
        self.interrupt()
