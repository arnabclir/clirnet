# Performance Improvement TODO List for MedWiki Facts Extractor


## Overview

The current implementation processes medical articles sequentially, leading to long processing times when handling multiple articles. Each article requires an API call to MiniMax-M2, which can take several seconds to complete. Additionally, results are only saved at the end of the entire process, which risks losing all processed data if the process is interrupted. Below are actionable improvements to enhance performance and reliability.


## Immediate Improvements

### 1. Implement True Parallel Processing
**Problem**: Current batch processor runs API calls sequentially with only artificial delays between requests.
**Solution**: Use asyncio with `asyncio.gather()` to process multiple articles concurrently within rate limits.
**Details**: 
- Modify `batch_processor.py` to create concurrent tasks
- Use `asyncio.Semaphore` to limit concurrent API calls to prevent rate limiting
- Process articles in batches of 4-8 concurrently (as defined by `batch_size` parameter)

### 2. Optimize Rate Limiting Strategy
**Problem**: Fixed 0.5s delay between all requests regardless of actual API rate limits.
**Solution**: Implement dynamic rate limiting based on API response headers or actual usage.
**Details**:
- Monitor MiniMax API rate limit headers
- Adjust delay dynamically based on remaining quota
- Implement exponential backoff for rate limit errors


### 3. Implement Incremental Result Saving
**Problem**: Results are only saved at the end of processing, risking data loss if the process is interrupted.
**Solution**: Save results incrementally after each successful inference call.
**Details**:
- Write successful results to output file immediately after each API call
- Use atomic file operations to prevent corruption
- Maintain a separate progress log to track completed articles



## Medium-term Improvements

### 4. Add Result Caching
**Problem**: All articles are reprocessed even if some were already completed successfully.
**Solution**: Cache successful results and skip reprocessing on subsequent runs.
**Details**:
- Check for existing results before processing an article
- Add a `--resume` flag to continue from the last successful article
- Implement cache validation to ensure data integrity


### 4. Implement Progress Tracking and Resumable Processing
**Problem**: If processing is interrupted, all progress is lost and the entire batch must be restarted.
**Solution**: Add checkpointing functionality to save progress periodically.
**Details**:
- Save results after each batch completion
- Track which articles have been processed in a separate file
- Allow restarting from the last checkpoint

### 5. Optimize JSON Processing
**Problem**: JSON parsing and serialization adds overhead, especially with the fallback error handling.
**Solution**: Streamline JSON processing and reduce unnecessary conversions.
**Details**:
- Avoid double JSON parsing in `extractor.py`
- Consider using faster JSON libraries like `orjson`
- Optimize the structure of data passed between functions

### 6. Add Article Preprocessing
**Problem**: Long articles may take longer to process and don't benefit from content optimization.
**Solution**: Implement preprocessing to clean and optimize article content before sending to API.
**Details**:
- Remove redundant HTML entities
- Trim excessive whitespace
- Split very long articles into segments if beneficial

## Long-term Improvements

### 7. Model Selection Optimization
**Problem**: MiniMax-M2 may not be the fastest model for this extraction task.
**Solution**: Experiment with alternative models that offer better speed/quality trade-offs.
**Details**:
- Test different models (GPT-4, Claude, Llama variations)
- Measure processing time vs. quality for each model
- Allow model selection via command-line parameter

### 8. Batch API Implementation
**Problem**: Each article requires a separate API call, which is inefficient.
**Solution**: Use batch processing endpoints if available from the API provider.
**Details**:
- Research MiniMax batch processing APIs
- Implement batch request formation
- Handle batch response parsing appropriately


## Implementation Priority



1. **High Priority**: Incremental result saving - prevents data loss during long processing runs
2. **High Priority**: True parallel processing - directly addresses the main performance bottleneck

3. **High Priority**: Caching and resumable processing - prevents rework and saves time
4. **Medium Priority**: Dynamic rate limiting - prevents failures and optimizes request timing

5. **Medium Priority**: JSON optimization - reduces processing overhead

6. **Low Priority**: Model testing - exploration for potential future optimization

7. **Low Priority**: Batch API usage - dependent on provider support


## Expected Performance Gains


- **Parallel Processing**: 4-8x speed improvement (processing 4-8 articles concurrently)

- **Incremental Result Saving**: Eliminates risk of data loss during processing
- **Caching**: Eliminates reprocessing time for completed articles

- **Optimized Rate Limiting**: Reduces unnecessary delays between requests

- **JSON Optimization**: Minor but measurable reduction in processing overhead


## Testing Strategy

1. Process a small subset of articles (5-10) with current implementation
2. Implement parallel processing and compare time
3. Add caching and test interruption/resume scenarios
4. Validate that all extracted information remains accurate despite performance improvements
