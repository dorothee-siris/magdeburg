# lib/data_cache.py
"""
Centralized data loading with Streamlit caching.
All parquet files are loaded once and shared across views.
"""
from __future__ import annotations
from pathlib import Path
import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


@st.cache_resource
def get_topics_df() -> pd.DataFrame:
    """Taxonomy: domains, fields, subfields, topics (all_topics.parquet)."""
    return pd.read_parquet(DATA_DIR / "all_topics.parquet")

@st.cache_data
def load_thematic_overview():
    return pd.read_parquet("data/thematic_overview.parquet")

@st.cache_data
def load_thematic_sublevels():
    return pd.read_parquet("data/thematic_detail_sublevels.parquet")

@st.cache_data
def load_thematic_contributions():
    return pd.read_parquet("data/thematic_detail_contributions.parquet")

@st.cache_data
def load_thematic_partners():
    return pd.read_parquet("data/thematic_detail_partners.parquet")

@st.cache_data
def load_thematic_authors():
    return pd.read_parquet("data/thematic_detail_authors.parquet")

@st.cache_data
def load_tm_labels():
    """Load topic model labels and keywords."""
    try:
        return pd.read_parquet("data/TM_labels.parquet")
    except Exception as e:
        return pd.DataFrame()
    
@st.cache_data
def load_treemap_hierarchy():
    return pd.read_parquet("data/treemap_hierarchy.parquet")