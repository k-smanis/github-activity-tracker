from pydantic import BaseModel, Field, HttpUrl
from enum import Enum
from datetime import datetime


class EventType(Enum):
    CommitCommentEvent = "CommitCommentEvent"
    CreateEvent = "CreateEvent"
    DeleteEvent = "DeleteEvent"
    DiscussionEvent = "DiscussionEvent"
    ForkEvent = "ForkEvent"
    GollumEvent = "GollumEvent"
    IssueCommentEvent = "IssueCommentEvent"
    IssuesEvent = "IssuesEvent"
    MemberEvent = "MemberEvent"
    PublicEvent = "PublicEvent"
    PullRequestEvent = "PullRequestEvent"
    PullRequestReviewEvent = "PullRequestReviewEvent"
    PullRequestReviewCommentEvent = "PullRequestReviewCommentEvent"
    PushEvent = "PushEvent"
    ReleaseEvent = "ReleaseEvent"
    WatchEvent = "WatchEvent"


class Actor(BaseModel):
    id: int
    login: str
    display_login: str
    gravatar_id: str
    url: HttpUrl
    avatar_url: HttpUrl


class Org(BaseModel):
    id: int
    login: str
    gravatar_id: str
    url: HttpUrl
    avatar_url: HttpUrl


class Repo(BaseModel):
    id: int
    name: str
    url: HttpUrl


class Payload(BaseModel):
    pass


class CommitCommentEventPayload(Payload):
    action: str | None = Field(default=None)
    comment: dict | None = Field(default=None)


class CreateEvent(Payload):
    ref: str | None = Field(default=None)
    ref_type: str | None = Field(default=None)
    full_ref: str | None = Field(default=None)
    master_branch: str | None = Field(default=None)
    description: str | None = Field(default=None)
    pusher_type: str | None = Field(default=None)


class DeleteEvent(Payload):
    ref: str | None = Field(default=None)
    ref_type: str | None = Field(default=None)
    full_ref: str | None = Field(default=None)
    pusher_type: str | None = Field(default=None)


class DiscussionEvent(Payload):
    action: str | None = Field(default=None)
    discussion: dict | None = Field(default=None)


class ForkEvent(Payload):
    action: str | None = Field(default=None)
    forkee: dict | None = Field(default=None)


class GollumEvent(Payload):
    pages: list[dict] | None = Field(default=None)


class IssueCommentEvent(Payload):
    action: str | None = Field(default=None)
    issue: dict | None = Field(default=None)
    comment: dict | None = Field(default=None)


class IssuesEvent(Payload):
    action: str | None = Field(default=None)
    issue: dict | None = Field(default=None)
    assignee: dict | None = Field(default=None)
    assignees: list[dict] | None = Field(default=None)
    label: dict | None = Field(default=None)
    labels: list[dict] | None = Field(default=None)


class MemberEvent(Payload):
    action: str | None = Field(default=None)
    member: dict | None = Field(default=None)


class PublicEvent(Payload):
    pass  # empty payload object)


class PullRequestEvent(Payload):
    action: str | None = Field(default=None)
    number: int | None = Field(default=None)
    pull_request: dict | None = Field(default=None)
    assignee: dict | None = Field(default=None)
    assignees: list[dict] | None = Field(default=None)
    label: dict | None = Field(default=None)
    labels: list[dict] | None = Field(default=None)


class PullRequestReviewEvent(Payload):
    action: str | None = Field(default=None)
    pull_request: dict | None = Field(default=None)
    review: dict | None = Field(default=None)


class PullRequestReviewCommentEvent(Payload):
    action: str | None = Field(default=None)
    pull_request: dict | None = Field(default=None)
    comment: dict | None = Field(default=None)


class PushEvent(Payload):
    repository_id: int | None = Field(default=None)
    push_id: int | None = Field(default=None)
    ref: str | None = Field(default=None)
    head: str | None = Field(default=None)
    before: str | None = Field(default=None)


class ReleaseEvent(Payload):
    action: str | None = Field(default=None)
    release: dict | None = Field(default=None)


class WatchEvent(Payload):
    action: str | None = Field(default=None)


class Event(BaseModel):
    id: str
    type: EventType
    actor: Actor
    repo: Repo
    payload: Payload
    public: bool
    created_at: datetime
    org: Org | None


class Activity(BaseModel):
    events: list[Event]
